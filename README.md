# PENIOT: PENIOT: Penetration Testing Tool for IoT

## Project Description

### What is PENIOT?

PENIOT is a penetration testing tool for Internet of Things (IoT) devices. 
It helps you to test/penetrate your devices by targeting their internet connectivity
with different types of security attacks. In other words, you can expose your device
to both active and passive security attacks. After deciding target device and necessary
information (or parameters) of that device, you can perform active security attacks like
altering/consuming system resources, replaying valid communication units and so on.
Also, you can perform passive security attacks such as breaching of confidentiality of
important information or reaching traffic analysis. Thanks to PENIOT, all those operations
can be semi-automated or even fully automated. In short, PENIOT is a package/framework for
targeting IoT devices with protocol based security attacks.

Also, it gives you a baseline structure for your further injections of new security attacks
or new IoT protocols. One of the most important features of PENIOT is being extensible.
By default, it has several common IoT protocols and numerous security attacks related to
those protocols. But, it can be extended further via exporting basic structure of internally
used components so that you can develop your attacks in harmony with the internal structure
of the PENIOT. 

### Why is PENIOT required?

The IoT paradigm has experienced immense growth in the past decade, with billions of devices
connected to the Internet. Most of these devices lack even basic security measures due to
their capacity constraints and designs made without security in mind due to the shortness
of time-to-market. Due to the high connectivity in IoT, attacks that have devastating
effects in extended networks can easily be launched by hackers through vulnerable devices.

Up until now, penetration testing was done manually if it was not ignored at all.
This procedure made testing phase of devices very slow. On the other hand, the firms which
produce IoT devices should always be up to date on testing their devices in terms of
reliability, robustness as well as their provided functionalities since being exposed to
security attacks by malicious people could cause unexpected impacts on end-users.
The main aim of PENIOT is to accelerate the process of security testing. It enables you to
figure out security flaws on your IoT devices by automating the time consuming penetration
testing phase.


### What does PENIOT provide?

First of all, PENIOT provides novelty. It is one of the first examples of penetration testing
tools on IoT field. There are only one or two similar tools which are specialized on IoT,
but they are still on development phase, so not completed yet.

Since the number of IoT devices is increasing drastically, IoT devices become more and more
common in our daily life. Smart homes, smart bicycles, medical sensors, fitness trackers,
smart locks and connected factories are just a few examples of IoT products. Given this,
we felt the need to choose some of the most commonly used IoT protocols to plant into PENIOT
by default. We chose the following protcols as the default IoT protocols included in the
PENIOT. These IoT protocols are tested with various types of security attacks such as DoS,
Fuzzing, Sniffing and Replay attacks. 

Following protocols are currently supported:
* Advanced Message Queuing Protocol ([AMQP](https://www.amqp.org/))
* Bluetooth Low Energy ([BLE](https://www.bluetooth.com/))
* Constraint Application Protocol ([CoAP](https://coap.technology/))
* Message Queuing Telemetry Transport ([MQTT](http://mqtt.org/))

Moreover, it enables you to export internal mainframe of its own implemented protocol and
attacks to implement your own protocols or attacks. Also, you can extend already existing
protocols with your newly implemented attacks. And lastly, it provides you an easy to use,
user friendly graphical user interface. 

### Build instructions
You can build project in your local by executing following codes.
```shell
$ git clone git@github.com:yakuza8/peniot.git
$ cd peniot
$ python setup.py install
```
Even if we provide you up-to-date installation script, there can be some missing parts in
it since the project cannot be maintained so long. Please inform us if there is any problem
with installation.

### Documentation
You can find *Design Overview Document* and *Final Design Document* under the **resources/documents** folder.
Several diagrams are attached under the **resources/diagrams** folder. Here is the simplest
representation of how PENIOT is separated modules and how it is designed.

<p align="center">
<img src="/resources/diagrams/peniot_structure_component_diagram.png">
</p>

## Project Poster
<p align="center">
<img src="/resources/peniot_vectorized.svg">
</p>