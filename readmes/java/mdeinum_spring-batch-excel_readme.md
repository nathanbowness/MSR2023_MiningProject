# spring-batch-excel

The code for this project is now part of the https://github.com/spring-projects/spring-batch-extensions[Spring Batch Extensions] project and is thus no longer activily maintained here. Please redirect issues and likes to that repository.  

image::https://api.codacy.com/project/badge/Grade/c52a51f788a543a9964cb8a148cfcd92[Codacy Badge]

Spring Batch extension which contains an `ItemReader` implementation for Excel based on https://poi.apache.org[Apache POI]. It supports reading both XLS and XLSX files, for the latter there is also (experimental) streaming support.

The `PoiItemReader` has the most features but is also the most memory intensive and might lead to memory issues with large XLS(X) sheets.

To reduce the memory footprint the `StreamingXlsxItemReader` can be used, this will only keep the current row in memory and discard it afterwards. Not everything is supported while streaming the XLSX file, it can be that formulas don't get evaluated or lead to an error.

## Configuration of `PoiItemReader`

Next to the https://docs.spring.io/spring-batch/reference/html/configureJob.html[configuration of Spring Batch] one needs to configure the `PoiItemReader`.

Configuration of can be done in XML or Java Config.

### XML

```xml
 <bean id="excelReader" class="org.springframework.batch.extensions.excel.poi.PoiItemReader" scope="step">
     <property name="resource" value="file:/path/to/your/excel/file" />
     <property name="rowMapper">
         <bean class="org.springframework.batch.extensions.excel.mapping.PassThroughRowMapper" />
     </property>
 </bean>
```

### Java Config

```java
@Bean
@StepScope
public PoiItemReader excelReader() {
    PoiItemReader reader = new PoiItemReader();
    reader.setResource(new FileSystemResource("/path/to/your/excel/file"));
    reader.setRowMapper(rowMapper());
    return reader;
}

@Bean
public RowMapper rowMapper() {
    return new PassThroughRowMapper();
}
```

## Configuration of `StreamingXlsxItemReader`

Configuration can be done in XML or Java Config.

### XML

```xml
 <bean id="excelReader" class="org.springframework.batch.extensions.excel.streaming.StreamingXlsxItemReader" scope="step">
     <property name="resource" value="file:/path/to/your/excel/file" />
     <property name="rowMapper">
         <bean class="org.springframework.batch.extensions.excel.mapping.PassThroughRowMapper" />
     </property>
 </bean>
```

### Java Config

```java
@Bean
@StepScope
public StreamingXlsxItemReader excelReader() {
    StreamingXlsxItemReader reader = new StreamingXlsxItemReader();
    reader.setResource(new FileSystemResource("/path/to/your/excel/file"));
    reader.setRowMapper(rowMapper());
    return reader;
}

@Bean
public RowMapper rowMapper() {
    return new PassThroughRowMapper();
}
```


## Configuration properties
[cols="1,1,1,4"]
.Properties for item readers
|===
| Property | Required | Default | Description

| `endAfterBlankLines` | no | 1 | The number of blank lines before stopping to read.
| `linesToSkip` | no | 0 | The number of lines to skip, this applies to each sheet in the Excel file, can be useful if the first couple of lines provide header information.
| `password` | no | `null` | The password used to protect an XLS file. Only works for XLS files not XLSX files (not supported with streaming).
| `resource` | yes | `null` | Location of the excel file to read, can be any resource supported by Spring.
| `rowMapper` | yes | `null` | transforms the rows read from the sheet(s) to an object which you can use in the rest of the process.
| `rowSetFactory` | no | `DefaultRowSetFactory` | For reading rows a `RowSet` abstraction is used. To construct a `RowSet` for the current `Sheet` a `RowSetFactory` is needed. The `DefaultRowSetFactory` constructs a `DefaultRowSet` and `DefaultRowSetMetaData`. For construction of the latter a `ColumnNameExtractor` is needed. At the moment there are 2 implementations
| `skippedRowsCallback` | no | `null` | When rows are skipped an optional `RowCallbackHandler` is called with the skipped row. This comes in handy when one needs to write the skipped rows to another file or create some logging.
| `strict` | no | `true` | This controls wether or not an exception is thrown if the file doesn't exists or isn't readable, by default an exception will be thrown.
|===

 - `StaticColumnNameExtractor` uses a preset list of column names.
 - `RowNumberColumnNameExtractor` (**the default**) reads a given row (default 0) to determine the column names of the current sheet

## RowMappers
To map a read row a `RowMapper` is needed. Out-of-the-box there are 2 implementations. The `PassThroughRowMapper` and `BeanWrapperRowMapper`.

### PassThroughRowMapper
Transforms the read row from excel into a `String[]`.

### BeanWrapperRowMapper
Uses a `BeanWrapper` to convert a given row into an object. Uses the column names of the given `RowSet` to map column to properties of the `targetType` or prototype bean.

```java
<bean id="excelReader" class="org.springframework.batch.extensions.excel.poi.PoiItemReader" scope="step">
    <property name="resource" value="file:/path/to/your/excel/file" />
    <property name="rowMapper">
        <bean class="org.springframework.batch.extensions.excel.mapping.BeanWrapperRowMapper">
            <property name="targetType" value="com.your.package.Player" />
        <bean>
    </property>
</bean>
```
