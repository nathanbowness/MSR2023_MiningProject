# Service Binding Specification for Kubernetes

Today in Kubernetes, the exposure of secrets for connecting application workloads to external services such as REST APIs, databases, event buses, and many more is manual and bespoke.  Each service provider suggests a different way to access their secrets, and application developers consume these secrets in a way specific to each workload.  While there is a good deal of value to this flexibility, large development teams lose overall velocity dealing with each unique solution.  To combat this, we see teams adopting internal patterns for how to achieve this workload-to-service linkage.

This specification aims to create a Kubernetes-wide specification for communicating service secrets to workloads in a consistent way.  It aims to create a widely applicable mechanism _without_ excluding other strategies for systems that it does not fit easily.  The benefit of Kubernetes-wide specification is that all of the actors in an ecosystem can work towards a clearly defined abstraction at the edge of their expertise and depend on other parties to complete the chain.

* Application Developers expect their secrets to be presented consistently and predictably within a container.
* Service Providers expect their secrets to be collected and exposed to consumers consistently and predictably.
* Platforms expect to retrieve secrets from Service Providers and expose them to Application Developers consistently and predictably.

The pattern of Service Binding has prior art in non-Kubernetes platforms.  Heroku pioneered this model with [Add-ons][h], and Cloud Foundry adopted similar ideas with their [Services][cf].  Other open source projects like the [Open Service Broker][osb] aim to help with this pattern on those non-Kubernetes platforms.  In the Kubernetes ecosystem, the CNCF Sandbox Cloud Native Buildpacks project has proposed a [buildpack-specific specification][cnb] exclusively addressing the application developer portion of this pattern.

[h]: https://devcenter.heroku.com/articles/add-ons
[cf]: https://docs.cloudfoundry.org/devguide/services/
[osb]: https://www.openservicebrokerapi.org
[cnb]: https://github.com/buildpacks/spec/blob/master/extensions/bindings.md

<!-- omit in toc -->
## Community, discussion, contribution, and support

The Service Binding Specification for Kubernetes project is a community lead effort.
A bi-weekly [working group call][working-group] is open to the public.
Discussions occur here on GitHub and on the [#bindings-discuss channel in the Kubernetes Slack][slack].

If you catch an error in the specification’s text, or if you write an
implementation, please let us know by opening an issue or pull request at our
[GitHub repository][repo].

<!-- omit in toc -->
### Code of conduct

Participation in the Service Binding community is governed by the [Contributor Covenant][code-of-conduct].

[working-group]: https://docs.google.com/document/d/1rR0qLpsjU38nRXxeich7F5QUy73RHJ90hnZiFIQ-JJ8/edit#heading=h.ar8ibc31ux6f
[slack]: https://kubernetes.slack.com/archives/C012F2GPMTQ
[repo]: https://github.com/servicebinding/spec
[code-of-conduct]: ./CODE_OF_CONDUCT.md

---

<!-- Using https://github.com/yzhang-gh/vscode-markdown to manage toc -->
- [Service Binding Specification for Kubernetes](#service-binding-specification-for-kubernetes)
  - [Status](#status)
  - [Notational Conventions](#notational-conventions)
  - [Terminology definition](#terminology-definition)
- [Provisioned Service](#provisioned-service)
  - [Resource Type Schema](#resource-type-schema)
  - [Example Resource](#example-resource)
  - [Well-known Secret Entries](#well-known-secret-entries)
  - [Example Secret](#example-secret)
  - [Considerations for Role-Based Access Control (RBAC)](#considerations-for-role-based-access-control-rbac)
    - [Example Resource](#example-resource-1)
- [Workload Projection](#workload-projection)
  - [Example Directory Structure](#example-directory-structure)
  - [Considerations for Role-Based Access Control (RBAC)](#considerations-for-role-based-access-control-rbac-1)
    - [Example Resource](#example-resource-2)
- [Service Binding](#service-binding)
  - [Resource Type Schema](#resource-type-schema-1)
  - [Minimal Example Resource](#minimal-example-resource)
  - [Label Selector Example Resource](#label-selector-example-resource)
  - [Environment Variables Example Resource](#environment-variables-example-resource)
  - [Reconciler Implementation](#reconciler-implementation)
    - [Ready Condition Status](#ready-condition-status)
    - [ServiceAvailable Condition Status](#serviceavailable-condition-status)
- [Direct Secret Reference](#direct-secret-reference)
  - [Direct Secret Reference Example Resource](#direct-secret-reference-example-resource)
- [Workload Resource Mapping](#workload-resource-mapping)
  - [Fixed JSONPath](#fixed-jsonpath)
  - [Resource Type Schema](#resource-type-schema-2)
  - [Example Resource](#example-resource-3)
  - [`PodSpec`-able (Default) Example Resource](#podspec-able-default-example-resource)
  - [Runtime Behavior](#runtime-behavior)
- [Role-Based Access Control (RBAC)](#role-based-access-control-rbac)
  - [Example Resource](#example-resource-4)

---

## Status

This document is a working draft of the Service Bindings for Kubernetes specification, representing the collective efforts of the [community](#community).  It is published for early implementors and users to provide feedback.  [Releases of the specification][releases] are published on the main website.

[releases]: https://servicebinding.io/#specification

## Notational Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) [RFC2119](https://tools.ietf.org/html/rfc2119) [RFC8174](https://tools.ietf.org/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

The key words "unspecified", "undefined", and "implementation-defined" are to be interpreted as described in the [rationale for the C99 standard](http://www.open-std.org/jtc1/sc22/wg14/www/C99RationaleV5.10.pdf#page=18).

An implementation is not compliant if it fails to satisfy one or more of the MUST, MUST NOT, REQUIRED, SHALL, or SHALL NOT requirements for the protocols it implements.  An implementation is compliant if it satisfies all the MUST, MUST NOT, REQUIRED, SHALL, and SHALL NOT requirements for the protocols it implements.

## Terminology definition

<dl>
  <dt>Duck Type</dt>
  <dd>Any type that meets the contract defined in a specification, without being an instance of a specific concrete type.  For example, for a specification that requires a given key on <code>status</code>, any resource that has that key on its <code>status</code> regardless of its <code>apiVersion</code> or <code>kind</code> would be considered to implement that duck type.</dd>

  <dt>Service</dt>
  <dd>Any software that exposes functionality.  Examples include a database, a message broker, a workload with REST endpoints, an event stream, an Application Performance Monitor, or a Hardware Security Module.</dd>

  <dt>Workload</dt>
  <dd>A <a href="https://kubernetes.io/docs/concepts/workloads/">workload</a> is an application running on Kubernetes.  Examples include processing using a framework like Spring Boot, NodeJS Express, or Ruby on Rails.  Workloads are the part of an application that runs.  Workloads may colloquially be referred to as an application.</dd>

  <dt>Service Binding</dt>
  <dd>The act of or representation of the action of providing information about a Service to a Workload</dd>

  <dt>Secret</dt>
  <dd>A Kubernetes <a href="https://kubernetes.io/docs/concepts/configuration/secret/"><code>Secret</code></a></dd>

  <dt><code>PodSpec</code>-able Duck Type</dt>
  <dd>A Kubernetes resource where <code>.spec.template</code> attribute comforms to a Kubernetes <a href="https://kubernetes.io/docs/concepts/workloads/pods/">Pod's spec</a>.  Examples of resources include DaemonSet, Deployment, Job, and StatefulSet.</dd>
</dl>

# Provisioned Service

A Provisioned Service resource **MUST** define a `.status.binding` field which is a `LocalObjectReference`-able (containing a single field `name`) to a `Secret`.  The `Secret` **MUST** exist in the same namespace as the resource.  The `Secret` data **SHOULD** contain a `type` entry with a value that identifies the abstract classification of the binding.  The `Secret` type (`.type` verses `.data.type` fields) **SHOULD** reflect this value as `servicebinding.io/{type}`, substituting `{type}` with the `Secret` data type.  It is **RECOMMENDED** that the `Secret` data also contain a `provider` entry with a value that identifies the provider of the binding.  The `Secret` data **MAY** contain any other entry.  To facilitate discoverability, it is **RECOMMENDED** that a `CustomResourceDefinition` exposing a Provisioned Service add `servicebinding.io/provisioned-service: "true"` as a label.

> Note: While the Provisioned Service referenced `Secret` data should contain a `type` entry, the `type` must be defined as it is projected to a workload.  The relaxation of the requirement for provisioned services allows for a mapping to enrich an existing secret.  For example, `ServiceBinding` has fields to override `type` and `provider` values.

Extensions and implementations **MAY** define additional mechanisms to consume a Provisioned Service that does not conform to the duck type.

## Resource Type Schema

```yaml
status:
  binding:
    name: # string
```

## Example Resource

```yaml
...
status:
  ...
  binding:
    name: production-db-secret
```

## Well-known Secret Entries

Other than the recommended `type` and `provider` entries, there are no other reserved `Secret` entries.  In the interests of consistency, if a `Secret` includes any of the following entry names, the entry value **MUST** meet the specified requirements:

| Name | Requirements
| ---- | ------------
| `host` | A DNS-resolvable host name or IP address
| `port` | A valid port number
| `uri` | A valid URI as defined by [RFC3986](https://tools.ietf.org/html/rfc3986)
| `username` | A string-based username credential
| `password` | A string-based password credential
| `certificates` | A collection of PEM-encoded X.509 public certificates, representing a certificate chain used to trust TLS connections
| `private-key` | A PEM-encoded private key used in mTLS client authentication

`Secret` entries that do not meet these requirements **MUST** use different entry names.

## Example Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: production-db-secret
type: servicebinding.io/mysql
stringData:
  type: mysql
  provider: bitnami
  host: localhost
  port: 3306
  username: root
  password: root
```

## Considerations for Role-Based Access Control (RBAC)

Cluster operators and CRD authors **SHOULD** opt-in resources to expose provisioned services by defining a `ClusterRole` with a label matching `servicebinding.io/controller=true`.  The `get`, `list`, and `watch` verbs **MUST** be granted in the `ClusterRole`.

See [Role-Based Access Control (RBAC)](#role-based-access-control-rbac) for how the `ClusterRole` is consumed.

### Example Resource

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: awesome-service-bindings
  labels:
    servicebinding.io/controller: "true" # matches the aggregation rule selector
rules:
- apiGroups:
  - awesome.example.com
  resources:
  - awesomeservices
  verbs:
  - get
  - list
  - watch
```

# Workload Projection

A projected binding **MUST** be volume mounted into a container at `$SERVICE_BINDING_ROOT/<binding-name>` with directory names matching the name of the binding.  Binding names **MUST** match `[a-z0-9\-\.]{1,253}`.  The `$SERVICE_BINDING_ROOT` environment variable **MUST** be declared and can point to any valid file system location.

The projected binding **MUST** contain a `type` entry with a value that identifies the abstract classification of the binding.  It is **RECOMMENDED** that the projected binding also contain a `provider` entry with a value that identifies the provider of the binding.  The projected binding data **MAY** contain any other entry. Directories under `$SERVICE_BINDING_ROOT` that do not contain a `type` entry **SHOULD** be ignored by the workload process at runtime.

The name of a binding entry file name **SHOULD** match `[a-z0-9\-\.]{1,253}`.  The contents of a binding entry may be anything representable as bytes on the file system including, but not limited to, a literal string value (e.g. `db-password`), a language-specific binary (e.g. a Java `KeyStore` with a private key and X.509 certificate), or an indirect pointer to another system for value resolution (e.g. `vault://production-database/password`).

The collection of files within the directory **MAY** change during the lifetime of the container or between container launches.

## Example Directory Structure

```plain
$SERVICE_BINDING_ROOT
├── account-database
│   ├── type
│   ├── provider
│   ├── uri
│   ├── username
│   └── password
└── transaction-event-stream
    ├── type
    ├── connection-count
    ├── uri
    ├── certificates
    └── private-key
```

## Considerations for Role-Based Access Control (RBAC)

Cluster operators and CRD authors **SHOULD** opt-in resources to binding projection by defining a `ClusterRole` with a label matching `servicebinding.io/controller=true`.  The `get`, `list`, `watch`, `update`, and `patch` verbs **MUST** be granted in the `ClusterRole`.

See [Role-Based Access Control (RBAC)](#role-based-access-control-rbac) for how the `ClusterRole` is consumed.

### Example Resource

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: awesome-service-bindings
  labels:
    servicebinding.io/controller: "true" # matches the aggregation rule selector
rules:
- apiGroups:
  - awesome.example.com
  resources:
  - awesomeworkloads
  verbs:
  - get
  - list
  - watch
  - update
  - patch
```

# Service Binding

A Service Binding describes the connection between a [Provisioned Service](#provisioned-service) and a [Workload Projection](#workload-projection).  It **MUST** be codified as a concrete resource type with API version `servicebinding.io/v1beta1` and kind `ServiceBinding`.  An implementation **MAY** support other versions of this specification which define additional API versions.  Multiple `ServiceBinding` objects can refer to the same service.  Multiple `ServiceBinding` objects can refer to the same workload.  For portability, the schema **MUST** comply to the exemplar CRD found [here][sb-crd].

> Note: Restricting service binding to resources within the same namespace is strongly recommended.  Implementations that choose to support cross-namespace service binding must provide a security model that prevents attacks like privilege escalation and secret enumeration, as well as a deterministic way to declare target namespaces.

A `ServiceBinding` **MUST** define a `.spec.workload` which is an `ObjectReference`-like declaration.  A `ServiceBinding` **MAY** define the workload reference by-name or by-[label selector][ls].  A name and selector **MUST NOT** be defined in the same reference.  A `ServiceBinding` **MUST** define a `.spec.service` which is an `ObjectReference`-like declaration to a Provisioned Service-able resource.  Extensions and implementations **MAY** allow additional kinds of workloads and services to be referenced.

The `ServiceBinding` **MAY** define `.spec.workload.containers`, to limit which containers in the workload are bound.  If `.spec.workload.containers` is defined, the value **MUST** be a list of strings.  Binding to a container is opt-in, unless `.spec.workload.containers` is undefined then all containers **MUST** be bound.  For each item in the containers list:
- a container matched by name **MUST** be bound
- values that do not match a container **SHOULD** be ignored

A `ServiceBinding` **MAY** define a `.spec.env` which is an array of `EnvMapping`.  An `EnvMapping` object **MUST** define `name` and `key` entries.  The `key` of an `EnvMapping` **MUST** refer to a binding `Secret` key name.  The value of this `Secret` entry **MUST** be configured as an environment variable on the resource represented by `workload`.

A `ServiceBinding` **MUST** define `.status.conditions` which is an array of `Condition` objects as defined in [meta/v1 Condition][mv1c].  At least one condition containing a `type` of `Ready` **MUST** be defined by the implementation.  The `Ready` condition **SHOULD** contain appropriate values.  As label selectors are inherently queries that return zero-to-many resources, it is **RECOMMENDED** that `ServiceBinding` authors use a combination of labels that yield a single resource, but implementors **MUST** handle each matching resource as if it was specified by name in a distinct `ServiceBinding`.  Partial failures **MUST** be aggregated and reported on the binding status's `Ready` condition.  A `ServiceBinding` **SHOULD** reflect the secret projected into the workload as `.status.binding.name`.

When updating the status of the `ServiceBinding`, the controller **MUST** set the value of `.status.observedGeneration` to the value of `.metadata.generation`.  The `.metadata.generation` field is always the current generation of the `ServiceBinding`, which is incremented by the API server when writes are made to the `ServiceBinding` spec field.  Therefore, consumers **SHOULD** compare the value of the observed and current generations to know if the status reflects the current resource definition.

[sb-crd]: servicebinding.io_servicebindings.yaml
[ls]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
[gt]: https://golang.org/pkg/text/template/#pkg-overview
[mv1c]: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#condition-v1-meta

## Resource Type Schema

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ServiceBinding
metadata:
  name: # string
  generation: # int64, defined by the Kubernetes control plane
  ...
spec:
  name: # string, optional, default: .metadata.name
  type: # string, optional
  provider: # string, optional
  service: # Provisioned Service resource ObjectReference-like
    apiVersion: # string
    kind: # string
    name: # string
  workload: # ObjectReference-like
    apiVersion: # string
    kind: # string
    name: # string, mutually exclusive with selector
    selector: # metav1.LabelSelector, mutually exclusive with name
    containers: # []string, optional
  env: # []EnvMapping, optional
  - name: # string
    key: # string

status:
  binding: # LocalObjectReference, optional
    name: # string
  conditions: # []metav1.Condition containing at least one entry for `Ready`
  observedGeneration: # int64
```

## Minimal Example Resource

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ServiceBinding
metadata:
  name: account-service
spec:
  service:
    apiVersion: com.example/v1alpha1
    kind: AccountService
    name: prod-account-service
  workload:
    apiVersion: apps/v1
    kind: Deployment
    name: online-banking
status:
  conditions:
  - type: Ready
    status: 'True'
    reason: 'Projected'
    message: ''
    lastTransitionTime: '2021-01-20T17:00:00Z'
```

## Label Selector Example Resource

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ServiceBinding
metadata:
  name: online-banking-frontend-to-account-service
spec:
  name: account-service
  service:
    apiVersion: com.example/v1alpha1
    kind: AccountService
    name: prod-account-service
  workload:
    apiVersion: apps/v1
    kind: Deployment
    selector:
      matchLabels:
        app.kubernetes.io/part-of: online-banking
        app.kubernetes.io/component: frontend
status:
  conditions:
  - type: Ready
    status: 'True'
    reason: 'Projected'
    message: ''
    lastTransitionTime: '2021-01-20T17:00:00Z'
```

## Environment Variables Example Resource

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ServiceBinding
metadata:
  name: account-service
spec:
  service:
    apiVersion: com.example/v1alpha1
    kind: AccountService
    name: prod-account-service
  workload:
    apiVersion: apps/v1
    kind: Deployment
    name: online-banking
  env:
  - name: ACCOUNT_SERVICE_HOST
    key: host
  - name: ACCOUNT_SERVICE_USERNAME
    key: username
  - name: ACCOUNT_SERVICE_PASSWORD
    key: password
status:
  binding:
    name: prod-account-service-projection
  conditions:
  - type: Ready
    status: 'True'
    reason: 'Projected'
    message: ''
    lastTransitionTime: '2021-01-20T17:00:00Z'
```

## Reconciler Implementation

A Reconciler implementation for the `ServiceBinding` type is responsible for binding the Provisioned Service binding `Secret` into a workload.  The `Secret` referred to by `.status.binding` on the resource represented by `service` **MUST** be mounted as a volume on the resource represented by `workload`.

If a `.spec.name` is set, the directory name of the volume mount **MUST** be its value.  If a `.spec.name` is not set, the directory name of the volume mount **SHOULD** be the value of `.metadata.name`.

For each container to be bound, if the `$SERVICE_BINDING_ROOT` environment variable has already been configured on the resource represented by `workload`, the Provisioned Service binding `Secret` **MUST** be mounted relative to that location.  If the `$SERVICE_BINDING_ROOT` environment variable has not been configured on the resource represented by `workload`, the `$SERVICE_BINDING_ROOT` environment variable **MUST** be set and the Provisioned Service binding `Secret` **MUST** be mounted relative to that location.  A **RECOMMENDED** value to use is `/bindings`.

The `$SERVICE_BINDING_ROOT` environment variable **MUST NOT** be reset if it is already configured on the resource represented by `workload`.

If a `.spec.type` is set, the `type` entry in the workload projection **MUST** be set to its value overriding any existing value.  If a `.spec.provider` is set, the `provider` entry in the workload projection **MUST** be set to its value overriding any existing value.

The `ServiceBinding` status **MUST** be updated for the result of an error when the implementation is unable to retry the binding, or user interaction is required to recover from the error.  For example, when updating a workload resource to project a binding a conflict **SHOULD NOT** be reflected because retrying may allow the update to succeed.  A not found error fetching the workload resource **SHOULD** be reflected as the error is not recoverable until the target workload resource is created.  An implementation **MAY** record an event as a result of any error.

### Ready Condition Status

If the service binding is completed successfully, the `Ready` condition status **MUST** be set to `True`.  If the service binding cannot be completed, including cases where the service or workload resource are not found or do not conform to the specification requirements, the `Ready` condition status **MUST** be set to `False`.  If the `Ready` condition status is neither actively `True` nor `False` it **SHOULD** be set to `Unknown`.

### ServiceAvailable Condition Status

If the referenced Provisioned Service exists and exposes a binding secret, the `ServiceAvailable` condition status **MUST** be set to `True`.  If the referenced Provisioned Service either does not exist, or it cannot be determined if the resource exists, the `ServiceAvailable` condition status **MUST** be set to `False` with a meaningful message.  If the `ServiceAvailable` condition status is neither actively `True` nor `False` it **SHOULD** be set to `Unknown`.

# Direct Secret Reference

There are scenarios where an appropriate resource conforming to the Provisioned Service duck-type does not exist, but there is a `Secret` available for binding.  This feature allows a `ServiceBinding` to directly reference a `Secret`.

When the `.spec.service.kind` attribute is `Secret` and `.spec.service.apiVersion` is `v1`, the `.spec.service.name` attribute **MUST** be treated as `.status.binding.name` for a Provisioned Service.

## Direct Secret Reference Example Resource

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ServiceBinding
metadata:
  name: account-service

spec:
  service:
    apiVersion: v1
    kind: Secret
    name: prod-account-service-secret
  workload:
    apiVersion: apps/v1
    kind: Deployment
    name: online-banking
status:
  binding:
    name: prod-account-service-reference
  conditions:
  - type: Ready
    status: 'True'
    reason: 'Projected'
    message: ''
    lastTransitionTime: '2021-01-20T17:00:00Z'
```

# Workload Resource Mapping

A workload resource mapping describes how to apply [service binding](#service-binding) transformations to a [workload projection](#workload-projection).  It **MUST** be codified as a concrete resource type (cluster scoped resource) with API version `servicebinding.io/v1beta1` and kind `ClusterWorkloadResourceMapping`.  An implementation **MAY** support other versions of this specification which define additional API versions.  For portability, the schema **MUST** comply to the exemplar CRD found [here][cwrm-crd].

A workload resource mapping **MUST** define its name using [CRD syntax][crd-syntax] (`<plural>.<group>`) for the resource that it defines a mapping for.  A workload resource mapping **MUST** define a `.spec.versions` which is an array of `MappingTemplate` fragments.

A `MappingTemplate` fragment **MUST** define at least one `version` entry that represents a version of the mapped resource.  The `version` entry **MAY** contain a `*` wildcard which indicates that this mapping should be used for any version that does not have a mapping explicitly defined for it.  A `MappingTemplate` fragment **MAY** define `annotations`, as a string containing a [Fixed JSONPath](#fixed-jsonpath) that describes the location of a map of annotations in the target resource.  If not specified, the default `annotations` expression **MUST** be appropriate for mapping to a `PodSpec`-able resource (`.spec.template.metadata.annotations`).  A `MappingTemplate` fragment **MAY** define `containers`, as an array of `MappingContainer` fragments.  If not specified, the default `MappingContainer` **MUST** be appropriate for mapping to a `PodSpec`-able resource.  A `MappingTemplate` fragment **MAY** define `volumes`, as a string containing a [Fixed JSONPath](#fixed-jsonpath) that describes the location of [`[]Volume`][volume] arrays in the target resource.  If not specified, the default `volumes` expression **MUST** be appropriate for mapping to a `PodSpec`-able resource (`.spec.template.spec.volumes`).

A `MappingContainer` fragment **MUST** define a `path` entry which is a string containing a [JSONPath][jsonpath] that references container like locations in the target resource.  The following expressions **MUST** be applied to each object matched by the path.  A `MappingTemplate` object **MAY** define `name`, as a string containing a [Fixed JSONPath](#fixed-jsonpath) that describes the location of a string in the target resource that names the container.  A `MappingTemplate` object **MAY** define `env`, as a string containing a [Fixed JSONPath](#fixed-jsonpath) that describes the location of [`[]EnvVar`][envvar] array in the target resource.  If not specified, the default `env` expression **MUST** be appropriate for mapping within an actual `Container` object (`.env`).  A `MappingTemplate` object **MAY** define `volumeMounts`, as a string containing a [Fixed JSONPath](#fixed-jsonpath) that describes the location of [`[]VolumeMount`][volumemount] array in the target resource.  If not specified, the default `env` expression **MUST** be appropriate for mapping within an actual `Container` object (`.volumeMounts`).

[cwrm-crd]: servicebinding.io_clusterworkloadresourcemappings.yaml
[container]: https://kubernetes.io/docs/reference/kubernetes-api/workloads-resources/container/
[crd-syntax]: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-a-customresourcedefinition
[envvar]: https://kubernetes.io/docs/reference/kubernetes-api/workloads-resources/container/#environment-variables
[jsonpath]: http://goessner.net/articles/JsonPath/
[volume]: https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume
[volumemount]: https://kubernetes.io/docs/reference/kubernetes-api/workloads-resources/container/#volumes

## Fixed JSONPath

> Note: Only expressions labeled as 'Fixed JSONPath' **MUST** conform to this requirement.  Other expressions **MAY** use the full JSONPath syntax.

A Fixed JSONPath is a subset of [JSONPath][jsonpath] expressions that **MUST NOT** use type and operators other than fields separated by the child operator. This grammar allows accessing nested fields via a single, fixed path.

For example, these expressions are allowed:

- `.name`
- `['name']`
- `.spec.template.spec.volumes`
- `.spec['template'].spec['volumes']`

All other types and operators are disallowed, including but not limited to:

- texts
- identifiers
- filters
- ints
- floats
- wildcards
- recursives
- unions
- bools

## Resource Type Schema

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ClusterWorkloadResourceMapping
metadata:
  name: # string
  generation: # int64, defined by the Kubernetes control plane
  ...
spec:
  versions: # []MappingTemplate
  - version: # string
    annotations: # string (Fixed JSONPath), optional
    containers: # []MappingContainer, optional
    - path: # string (JSONPath)
      name: # string (Fixed JSONPath), optional
      env: # string (Fixed JSONPath), optional
      volumeMounts: # string (Fixed JSONPath), optional
    volumes: # string (Fixed JSONPath), optional
```

## Example Resource

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ClusterWorkloadResourceMapping
metadata:
 name: cronjobs.batch
spec:
  versions:
  - version: "*"
    annotations: .spec.jobTemplate.spec.template.metadata.annotations
    containers:
    - path: .spec.jobTemplate.spec.template.spec.containers[*]
      name: .name
      env: .env # this is the default value
      volumeMounts: .volumeMounts # this is the default value
    - path: .spec.jobTemplate.spec.template.spec.initContainers[*]
      name: .name
      env: .env # this is the default value
      volumeMounts: .volumeMounts # this is the default value
    volumes: .spec.jobTemplate.spec.template.spec.volumes
```

## `PodSpec`-able (Default) Example Resource

```yaml
apiVersion: servicebinding.io/v1beta1
kind: ClusterWorkloadResourceMapping
metadata:
  name: deployments.apps
spec:
  versions:
  - version: "*"
    annotations: .spec.template.metadata.annotations
    containers:
    - path: .spec.template.spec.containers[*]
      name: .name
      env: .env
      volumeMounts: .volumeMounts
    - path: .spec.template.spec.initContainers[*]
      name: .name
      env: .env
      volumeMounts: .volumeMounts
    volumes: .spec.template.spec.volumes
```

> Note: This example is equivalent to not specifying a mapping or specifying an empty mapping.

## Runtime Behavior

When a `ClusterWorkloadResourceMapping` is defined in the cluster matching a workload resource it **MUST** be used to map the binding that type.  If no mapping is available for the type, the implementation **MUST** treat the workload resource as a `PodSpec`-able type.

When a service binding projection is removed, the controller **MUST** use the same mappings from the projection creation.  After a `ClusterWorkloadResourceMapping` resource is modified, each binding targeting the mapped workload type **MUST** be removed, then reattempted with the latest mapping.

If a `ServiceBinding` specifies `.spec.workload.containers` and a `MappingContainer` specifies a `name` expression, the resolved name **MUST** limit which containers in the workload are bound.  If either key is not defined, the container **SHOULD** be bound.

An implementation **MUST** create empty values at locations referenced by [Fixed JSONPaths](#fixed-jsonpath) that do not exist on the workload resource.  Values referenced by JSONPaths in both the `MappingTemplate` and `MappingContainer` fragments **MUST** be mutated by a `ServiceBinding` reconciler as if they were defined directly by a [`corev1.PodTemplateSpec`][cv1pts].  A reconciler **MUST** preserve fields on the workload resource that fall outside the specific fragments and types defined by the mapping.

[cv1pts]: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#podtemplatespec-v1-core

# Role-Based Access Control (RBAC)

Kubernetes clusters often utilize [Role-based access control (RBAC)][rbac] to authorize subjects to perform specific actions on resources.  When operating in a cluster with RBAC enabled, the service binding reconciler needs permission to read resources that provisioned a service and write resources that services are projected into.  This section defines a means for third-party CRD authors and cluster operators to expose resources to the service binding reconciler.  Cluster operators **MAY** impose additional access controls beyond RBAC.

If a service binding reconciler implementation is using Role-Based Access Control (RBAC) it **MUST** define an [aggregated `ClusterRole`][acr] with a label selector matching the label `servicebinding.io/controller=true`.  This `ClusterRole` **MUST** be bound (`RoleBinding` for a single namespace or `ClusterRoleBinding` if cluster-wide) to the subject the service binding reconciler runs as, typically a `ServiceAccount`.

[rbac]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
[acr]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles

## Example Resource

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ...
aggregationRule:
  clusterRoleSelectors:
  - matchLabels:
      servicebinding.io/controller: "true"
rules: [] # The control plane automatically fills in the rules
```
