# Siddhi 4.x Quick Start Guide

Siddhi is a cloud native Streaming and Complex Event Processing engine that understands Streaming SQL queries in order to capture events from diverse data sources, process them, detect complex conditions, and publish output to various endpoints in real time.

Siddhi is used by many companies including Uber, eBay, PayPal (via Apache Eagle), here [**Uber processed more than 20 billion events per day using Siddhi**](http://wso2.com/library/conference/2017/2/wso2con-usa-2017-scalable-real-time-complex-event-processing-at-uber?utm_source=gitanalytics&utm_campaign=gitanalytics_Jul17) for their fraud analytics use cases. Siddhi is also used in various analytics and integration platforms such as [Apache Eagle](https://eagle.apache.org/) as a policy enforcement engine, [WSO2 API Manager](https://wso2.com/api-management/) as analytics and throttling engine, [WSO2 Identity Server](https://wso2.com/identity-and-access-management/) as an adaptive authorization engine.

This quick start guide contains the following six sections:

1. **Domain** of Siddhi
2. Overview of Siddhi **architecture**
3. Using Siddhi for the first time
4. Siddhi ‘Hello World!’
5. Simulating Events
6. A bit of Stream Processing

## 1. Domain of Siddhi

Siddhi is an event driven system where all the data it consumes, processes and sends are modeled as events. Therefore, Siddhi can play a vital part in any event-driven architecture.   

As Siddhi works with events, first let's understand what an event is through an example. **If we consider transactions carried out via an ATM as a data stream, one withdrawal from it can be considered as an event**. This event contains data such as amount, time, account number, etc. Many such transactions form a stream.
![](../../images/quickstart/event-stream.png?raw=true "Event Stream")

Siddhi provides following functionalities,

* Streaming Data Analytics<br/>
  [Forrester](https://reprints.forrester.com/#/assets/2/202/'RES136545'/reports) defines Streaming Analytics as:<br/>
  > Software that provides analytical operators to **orchestrate data flow**, **calculate analytics**, and **detect patterns** on event data **from multiple, disparate live data sources** to allow developers to build applications that **sense, think, and act in real time**.

* Complex Event Processing (CEP)<br/>
  [Gartner’s IT Glossary](https://www.gartner.com/it-glossary/complex-event-processing) defines CEP as follows:<br/>
  >"CEP is a kind of computing in which **incoming data about events is distilled into more useful, higher level “complex” event data** that provides insight into what is happening."
  >
  >"**CEP is event-driven** because the computation is triggered by the receipt of event data. CEP is used for highly demanding, continuous-intelligence applications that enhance situation awareness and support real-time decisions."

* Streaming Data Integration<br/>
  > Streaming data integration is a way of integrating several systems by processing, correlating, and analyzing the data in memory, while continuously moving data in real-time from one system to another.

* Alerts & Notifications
  > The system to continuously monitor event streams, and send alerts and notifications, based on defined KPIs and other analytics.

* Adaptive Decision Making
  > A way to dynamically making real-time decisions based on predefined rules, the current state of the connected systems, and machine learning techniques.

Basically, Siddhi receives data event-by-event and processes them in real-time to produce meaningful information.

![](../../images/quickstart/siddhi-basic.png?raw=true "Siddhi Basic Representation")

Using the above Siddhi can be used to solve may use-cases as follows:

* Fraud Analytics
* Monitoring
* System Integration
* Anomaly Detection
* Sentiment Analysis
* Processing Customer Behavior
* .. etc

## 2. Overview of Siddhi architecture

![](../../images/siddhi-overview.png?raw=true "Overview")

As indicated above, Siddhi can:

+ Accept event inputs from many different types of sources.
+ Process them to transform, enrich, and generate insights.
+ Publish them to multiple types of sinks.

To use Siddhi, you need to write the processing logic as a **Siddhi Application** in the **Siddhi Streaming SQL** language which is discussed in the [section 4](#4-writing-first-siddhi-application). Here a Siddhi Application is a script file that contains business logic for a scenario.

When the **Siddhi application** is started, it:

1. Consumes data one-by-one as events.
2. Pipe the events to queries through various streams for processing.
3. Generates new events based on the processing done at the queries.
4. Finally, Sends newly generated events through output to streams.

## 3. Using Siddhi for the first time

In this section, we will be using the WSO2 Stream Processor(referred to as SP in the rest of this guide) — a server version of Siddhi that has a
sophisticated editor with a GUI (referred to as _**“Stream Processor Studio”**_) where you can write your query and simulate events
as a data stream.

**Step 1** — Install 
[Oracle Java SE Development Kit (JDK)](http://www.oracle.com/technetwork/java/javase/downloads/index.html) version 1.8. <br>
**Step 2** — [Set the JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/) environment 
variable. <br>
**Step 3** — Download the latest [WSO2 Stream Processor](http://wso2.com/analytics?utm_source=gitanalytics&utm_campaign=gitanalytics_Jul17). <br>
**Step 4** — Extract the downloaded zip and navigate to `<SP_HOME>/bin`. <br> (`SP_HOME` refers to the extracted folder) <br>
**Step 5** — Issue the following command in the command prompt (Windows) / terminal (Linux) 

```
For Windows: editor.bat
For Linux: ./editor.sh
```
For more details about WSO2 Stream Processor, see its [Quick Start Guide](https://docs.wso2.com/display/SP400/Quick+Start+Guide).

After successfully starting the Stream Processor Studio, the terminal in Linux should look like as shown below:

![](../../images/quickstart/after-starting-sp.png?raw=true "Terminal after starting WSO2 Stream Processor Text Editor")

After starting the WSO2 Stream Processor, access the Stream Processor Studio by visiting the following link in your browser.
```
http://localhost:9390/editor
```
This takes you to the Stream Processor Studio landing page.

![](../../images/quickstart/sp-studio.png?raw=true "Stream Processor Studio")

## 4. Siddhi ‘Hello World!’ 

Siddhi Streaming SQL is a rich, compact, easy-to-learn SQL-like language. **Let's first learn how to find the total** of values 
coming into a data stream and output the current running total value with each event. Siddhi has lot of in-built functions and extensions 
available for complex analysis, but to get started, let's use a simple one. You can find more information about the Siddhi grammar 
and its functions in the [Siddhi Query Guide](../query-guide/).

Let's **consider a scenario where we are loading cargo boxes into a ship**. We need to keep track of the total 
weight of the cargo added. **Measuring the weight of a cargo box when loading is considered an event**.

![](../../images/quickstart/loading-ship.jpeg?raw=true "Loading Cargo on Ship")

We can write a Siddhi program for the above scenario which has **4 parts**.

**Part 1 — Giving our Siddhi application a suitable name.** This is a Siddhi routine. In this example, let's name our application as 
_“HelloWorldApp”_

```
@App:name("HelloWorldApp")
```
**Part 2 — Defining the input stream.** The stream needs to have a name and a schema defining the data that each incoming event should contain.
The event data attributes are expressed as name and type pairs. In this example:

* The name of the input stream — _“CargoStream”_ <br>
This contains only one data attribute:
* The name of the data in each event — _“weight”_
* Type of the data _“weight”_ — int

```
define stream CargoStream (weight int);
```
**Part 3 - Defining the output stream.** This has the same info as the previous definition with an additional 
_totalWeight_ attribute that contains the total weight calculated so far. Here, we need to add a 
_"sink"_  to log the `OutputStream` so that we can observe the output values. (**Sink is the Siddhi way to publish 
streams to external systems.** This particular `log` type sink just logs the stream events. To learn more about sinks, see 
[sink](../query-guide/#sink))
```
@sink(type='log', prefix='LOGGER')
define stream OutputStream(weight int, totalWeight long);
```
**Part 4 — The actual Siddhi query.** Here we need to specify the following:

1. A name for the query — _“HelloWorldQuery”_
2. Which stream should be taken into processing — _“CargoStream”_
3. What data we require in the output stream — _“weight”_, _“totalWeight”_
4. How the output should be calculated - by calculating the *sum* of the the *weight*s  
5. Which stream should be populated with the output — _“OutputStream”_

```
@info(name='HelloWorldQuery')
from CargoStream
select weight, sum(weight) as totalWeight
insert into OutputStream;
```

![](../../images/quickstart/hello-query.png?raw=true "Hello World in Stream Processor Studio")

## 5. Simulating Events

The Stream Processor Studio has in-built support to simulate events. You can do it via the _“Event Simulator”_ 
panel at the left of the Stream Processor Studio. You should save your _HelloWorldApp_ by browsing to **File** -> 
**Save** before you run event simulation. Then click  **Event Simulator** and configure it as shown below.

![](../../images/quickstart/event-simulation.png?raw=true "Simulating Events in Stream Processor Studio")

**Step 1 — Configurations:**

* Siddhi App Name — _“HelloWorldApp”_
* Stream Name — _“CargoStream”_
* Timestamp — (Leave it blank)
* weight — 2 (or some integer)

**Step 2 — Click “Run” mode and then click “Start”**. This starts the Siddhi Application. 
If the Siddhi application is successfully started, the following message is printed in the Stream Processor Studio console:</br>
_“HelloWorldApp.siddhi Started Successfully!”_ 

**Step 3 — Click “Send” and observe the terminal** where you started WSO2 Stream Processor Studio. 
You can see a log that contains _“outputData=[2, 2]”_. Click **Send** again and observe a log with 
_“outputData=[2, 4]”_. You can change the value of the weight and send it to see how the sum of the weight is updated.

![](../../images/quickstart/log.png?raw=true "Terminal after sending 2 twice")

Bravo! You have successfully completed creating Siddhi Hello World! 

## 6. A bit of Stream Processing

This section demonstrates how to carry out **temporal window processing** with Siddhi.

Up to this point, we have been carrying out the processing by having only the running sum value in-memory. 
No events were stored during this process. 

[Window processing](../query-guide/#window)
is a method that allows us to store some events in-memory for a given period so that we can perform operations 
such as calculating the average, maximum, etc values within them.

Let's imagine that when we are loading cargo boxes into the ship **we need to keep track of the average weight of 
the recently loaded boxes** so that we can balance the weight across the ship. 
For this purpose, let's try to find the **average weight of last three boxes** of each event.

![](../../images/quickstart/siddhi-windows.png?raw=true "Terminal after sending 2 twice")

For window processing, we need to modify our query as follows:
```
@info(name='HelloWorldQuery') 
from CargoStream#window.length(3)
select weight, sum(weight) as totalWeight, avg(weight) as averageWeight
insert into OutputStream;
```

* `from CargoStream#window.length(3)` - Here, we are specifying that the last 3 events should be kept in memory for processing.
* `avg(weight) as averageWeight` - Here, we are calculating the average of events stored in the window and producing the 
average value as _"averageWeight"_ (Note: Now the `sum` also calculates the `totalWeight` based on the last three events).

We also need to modify the _"OutputStream"_ definition to accommodate the new _"averageWeight"_.

```
define stream OutputStream(weight int, totalWeight long, averageWeight double);
```

The updated Siddhi Application should look as shown below:

![](../../images/quickstart/window-processing-app.png?raw=true "Window Processing with Siddhi")

Now you can send events using the Event Simulator and observe the log to see the sum and average of the weights of the last three 
cargo events.

It is also notable that the defined `length window` only keeps 3 events in-memory. When the 4th event arrives, the 
first event in the window is removed from memory. This ensures that the memory usage does not grow beyond a specific limit. There are also other 
implementations done in Siddhi  to reduce the memory consumption. For more information, see [Siddhi Architecture](../architecture/).

To learn more about the Siddhi functionality, see [Siddhi Documentation](../).

If you have questions please post them on<a target="_blank" href="http://stackoverflow.com/search?q=siddhi">Stackoverflow</a> with <a target="_blank" href="http://stackoverflow.com/search?q=siddhi">"Siddhi"</a> tag.
