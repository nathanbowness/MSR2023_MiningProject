:spring_version: current
:spring_boot_version: 2.4.3
:Controller: https://docs.spring.io/spring/docs/{spring_version}/javadoc-api/org/springframework/stereotype/Controller.html
:DispatcherServlet: https://docs.spring.io/spring/docs/{spring_version}/javadoc-api/org/springframework/web/servlet/DispatcherServlet.html
:SpringApplication: https://docs.spring.io/spring-boot/docs/{spring_boot_version}/api/org/springframework/boot/SpringApplication.html
:View: https://docs.spring.io/spring/docs/{spring_version}/javadoc-api/org/springframework/web/servlet/View.html
:Model: https://docs.spring.io/spring/docs/{spring_version}/javadoc-api/org/springframework/ui/Model.html
:images: https://raw.githubusercontent.com/spring-guides/gs-handling-form-submission/main/images
:toc:
:icons: font
:source-highlighter: prettify
:project_id: gs-handling-form-submission

This guide walks you through the process of using Spring to create and submit a web form.

== What You Will build

In this guide, you will build a web form, which will be accessible at the following URL:
`http://localhost:8080/greeting`

Viewing this page in a browser will display the form. You can submit a greeting by
populating the `id` and `content` form fields. A results page will be displayed when the form is submitted.


== What You Need

:java_version: 11
include::https://raw.githubusercontent.com/spring-guides/getting-started-macros/main/prereq_editor_jdk_buildtools.adoc[]

include::https://raw.githubusercontent.com/spring-guides/getting-started-macros/main/how_to_complete_this_guide.adoc[]

[[scratch]]
== Starting with Spring Initializr

You can use this https://start.spring.io/#!type=maven-project&language=java&platformVersion=2.5.5&packaging=jar&jvmVersion=11&groupId=com.example&artifactId=handling-form-submission&name=handling-form-submission&description=Demo%20project%20for%20Spring%20Boot&packageName=com.example.handling-form-submission&dependencies=web,thymeleaf[pre-initialized project] and click Generate to download a ZIP file. This project is configured to fit the examples in this tutorial.

To manually initialize the project:

. Navigate to https://start.spring.io.
This service pulls in all the dependencies you need for an application and does most of the setup for you.
. Choose either Gradle or Maven and the language you want to use. This guide assumes that you chose Java.
. Click *Dependencies* and select *Spring Web* and *Thymeleaf*.
. Click *Generate*.
. Download the resulting ZIP file, which is an archive of a web application that is configured with your choices.

NOTE: If your IDE has the Spring Initializr integration, you can complete this process from your IDE.

NOTE: You can also fork the project from Github and open it in your IDE or other editor.

[[initial]]
== Create a Web Controller

In Spring's approach to building web sites, HTTP requests are handled by a controller.
These components are easily identified by the {Controller}[`@Controller`] annotation. The
`GreetingController` in the following listing (from
`src/main/java/com/example/handlingformsubmission/GreetingController.java`) handles GET
requests for `/greeting` by returning the name of a {View}[`View`] (in this case,
`greeting`). The following `View` is responsible for rendering the HTML content:

====
[source,java,tabsize=2]
----
include::complete/src/main/java/com/example/handlingformsubmission/GreetingController.java[]
----
====

This controller is concise and simple, but a lot is going on. The rest of this section
analyzes it step by step.

The mapping annotations let you map HTTP requests to specific controller methods. The two
methods in this controller are both mapped to `/greeting`. You can use `@RequestMapping`
(which, by default, maps all HTTP operations, such as `GET`, `POST`, and so forth).
However, in this case, the `greetingForm()` method is specifically mapped to `GET` by
using `@GetMapping`, while `greetingSubmit()` is mapped to `POST` with `@PostMapping`.
This mapping lets the controller differentiate the requests to the `/greeting` endpoint.

The `greetingForm()` method uses a {Model}[`Model`] object to expose a new `Greeting` to
the view template. The `Greeting` object in the following code (from
`src/main/java/com/example/handlingformsubmission/Greeting.java`) contains fields such as
`id` and `content` that correspond to the form fields in the `greeting` view and are used
to capture the information from the form:

====
[source,java,tabsize=2]
----
include::complete/src/main/java/com/example/handlingformsubmission/Greeting.java[]
----
====

The implementation of the method body relies on a view technology to perform server-side
rendering of the HTML by converting the view name (`greeting`) into a template to render.
In this case, we use https://www.thymeleaf.org/doc/html/Thymeleaf-Spring3.html[Thymeleaf],
which parses the `greeting.html` template and evaluates the various template expressions
to render the form. The following listing (from
`src/main/resources/templates/greeting.html`) shows the `greeting` template:

====
[source,html]
----
include::complete/src/main/resources/templates/greeting.html[]
----
====

The `th:action="@{/greeting}"` expression directs the form to POST to the `/greeting`
endpoint, while the `th:object="${greeting}"` expression declares the model object to use
for collecting the form data. The two form fields, expressed with `th:field="*{id}"` and
`th:field="*{content}"`, correspond to the fields in the `Greeting` object.

That covers the controller, model, and view for presenting the form. Now we can review the
process of submitting the form. As noted earlier, the form submits to the `/greeting`
endpoint by using a `POST` call. The `greetingSubmit()` method receives the `Greeting`
object that was populated by the form. The `Greeting` is a `@ModelAttribute`, so it is
bound to the incoming form content. Also, the submitted data can be rendered in the
`result` view by referring to it by name (by default, the name of the method parameter, so
`greeting` in this case). The `id` is rendered in the
`<p th:text="'id: ' + ${greeting.id}" />` expression. Likewise, the `content` is rendered
in the `<p th:text="'content: ' + ${greeting.content}" />` expression. The following
listing (from `src/main/resources/templates/result.html`) shows the result template:

====
[source,html]
----
include::complete/src/main/resources/templates/result.html[]
----
====

For clarity, this example uses two separate view templates for rendering the form and
displaying the submitted data. However, you can use a single view for both purposes.


== Make the Application Executable

Although you can package this service as a traditional WAR file for deployment to an
external application server, the simpler approach is to create a standalone application.
You package everything in a single, executable JAR file, driven by a good old Java
`main()` method. Along the way, you use Spring's support for embedding the Tomcat servlet
container as the HTTP runtime, instead of deploying to an external instance. The following
listing (from
`src/main/java/com/example/handlingformsubmission/HandlingFormSubmissionApplication.java`)
shows the application class:

====
[source,java,tabsize=2]
----
include::complete/src/main/java/com/example/handlingformsubmission/HandlingFormSubmissionApplication.java[]
----
====

include::https://raw.githubusercontent.com/spring-guides/getting-started-macros/main/spring-boot-application-new-path.adoc[]

include::https://raw.githubusercontent.com/spring-guides/getting-started-macros/main/build_an_executable_jar_subhead.adoc[]

include::https://raw.githubusercontent.com/spring-guides/getting-started-macros/main/build_an_executable_jar_with_both.adoc[]

Logging output is displayed. The service should be up and running within a few seconds.


== Test the service

Now that the web site is running, visit http://localhost:8080/greeting, where you see the
following form:

image::{images}/form.png[Form]

Submit an ID and message to see the results:

image::{images}/result.png[Result]

== Summary

Congratulations! You have just used Spring to create and submit a form.

== See Also

The following guides may also be helpful:

* https://spring.io/guides/gs/validating-form-input/[Validating Form Input]
* https://spring.io/guides/gs/uploading-files/[Uploading Files]

include::https://raw.githubusercontent.com/spring-guides/getting-started-macros/main/footer.adoc[]
