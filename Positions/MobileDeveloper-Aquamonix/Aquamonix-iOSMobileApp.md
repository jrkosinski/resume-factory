# Aquamonix / Xamarin iOS Mobile Developer

## Basic Info

**Client / Employer:** Aquamonix
**Domain:** Industrial automation, SCADA, agricultural irrigation, IoT, mobile control systems
**Role / Title:** Mobile Developer / iOS Architect (exact title to be confirmed)
**Location:** Remote (client based in Australia)
**Dates:** 2015 – 2017
**Ownership:** Sole or lead developer — built MVP from scratch, designed architecture
**Status:** Completed
**Primary Stack:** C#, Xamarin, iOS, Objective-C, WebSockets
**Integration:** Java middle tier, SCADA irrigation systems

---

## Canonical Summary

Designed and built from scratch a Xamarin iOS application for Aquamonix, an Australian company that produces mobile-app-controlled industrial irrigation systems. The app controlled large-scale SCADA irrigation infrastructure through a Java middle tier. Architected the MVP, designed a cross-platform portability plan for future Android/other builds, and engineered a robust system for synchronizing long-running tasks with the server across multiple connections and app sessions — a technically demanding real-time coordination problem in an industrial control context. Stack: C#, Xamarin, iOS, Objective-C, WebSockets.

---

## Short Resume Summary Version

Sole/lead developer for Aquamonix's Xamarin iOS SCADA irrigation control app (2015–2017), building the product from scratch, architecting the MVP, designing cross-platform port strategy, and implementing long-running task synchronization across multiple WebSocket connections and app sessions.

---

## Primary Tags

* Xamarin
* iOS
* Objective-C
* C#
* WebSockets
* SCADA
* Industrial automation
* Irrigation control
* IoT
* Real-time systems
* Mobile architecture
* MVP development
* Cross-platform planning
* Long-running task synchronization
* Java middle tier integration
* Mobile from scratch
* Industrial mobile app
* Agriculture tech

---

## Context

Aquamonix is an Australian company that produces automated, mobile-app-controlled industrial irrigation systems. Their platform allows operators to control large-scale SCADA (Supervisory Control and Data Acquisition) irrigation infrastructure from a mobile device — a demanding domain that requires reliable real-time communication, robust handling of intermittent connectivity, and precise control over long-running physical processes (irrigation jobs).

The mobile app needed to communicate with a Java middle tier that interfaces with the underlying SCADA hardware. Unlike consumer apps, errors or synchronization failures in this context have direct consequences for physical infrastructure — irrigation schedules, valve states, water delivery — which makes reliability, state consistency, and session handling critical engineering concerns.

The Aquamonix engagement overlapped in dates with the FreshDirect/Door3 engagement (2014–2016), suggesting these were concurrent or sequential consulting projects.

---

## Role and Ownership

Served as the sole or lead developer for the Aquamonix iOS application, taking the product from zero to MVP.

Owned:

* Full greenfield build of the Xamarin iOS application
* MVP architecture design
* Cross-platform portability planning (for future Android/other ports)
* Long-running task synchronization system (multi-connection, multi-session)
* WebSocket communication layer
* Integration with the Java middle tier
* Objective-C interop within the Xamarin iOS environment

---

## Technical Work

### Greenfield Xamarin iOS Application

Built the Aquamonix mobile app from scratch using Xamarin and C#, targeting iOS. This was not a port or extension of an existing app — the application was designed and implemented from the ground up, covering UI, business logic, communication, and state management.

### SCADA Integration via Java Middle Tier

The app communicated with large-scale SCADA irrigation systems through a Java middle tier rather than directly to hardware. The mobile app acted as the control surface for the SCADA layer, sending commands and receiving state updates through this intermediary.

### MVP Architecture and Cross-Platform Plan

Architected the MVP with future cross-platform expansion in mind. Designed and documented a plan to facilitate cross-platform ports (e.g., Android), ensuring the architecture would not need to be fully rethought for each new platform — important for a small company investing in a long-lived product.

### Long-Running Task Synchronization

Engineered a synchronization system for long-running tasks across multiple connections and app sessions. This is a non-trivial problem in an industrial control context: irrigation jobs can run for extended periods, the app may be backgrounded or closed and reopened, and multiple connections may be active simultaneously. The system needed to maintain consistent task state across all of these scenarios reliably.

This was the most technically distinctive part of the engagement — a custom real-time state synchronization layer designed specifically for the constraints of mobile-to-SCADA control.

### WebSockets

Used WebSockets as the communication protocol for real-time bidirectional communication between the mobile app and the Java middle tier — appropriate for the low-latency, persistent-connection requirements of an interactive SCADA control surface.

---

# Bullet Bank

## Strong General Bullets

* Built Aquamonix's Xamarin iOS application from scratch — a mobile control interface for large-scale SCADA irrigation systems communicating through a Java middle tier.

* Architected the MVP for Aquamonix's industrial irrigation control app and designed a cross-platform portability plan to support future Android and other platform ports.

* Engineered a robust long-running task synchronization system that maintained consistent irrigation job state across multiple WebSocket connections and app sessions — a critical reliability requirement in an industrial control context.

* Delivered a full greenfield Xamarin iOS app in C# and Objective-C using WebSockets for real-time communication with a Java-backed SCADA control layer.

---

## Architecture / Design Bullets

* Designed the MVP architecture for a Xamarin iOS SCADA control app and produced a cross-platform portability plan to enable future Android and other platform builds without full architectural rethink.

* Architected real-time state synchronization for long-running industrial tasks across multiple simultaneous connections and app sessions using WebSockets.

---

## Mobile / Xamarin Bullets

* Built a Xamarin iOS application from zero using C# and Objective-C interop, targeting a specialized industrial control use case rather than a consumer experience.

* Used Xamarin as the primary development platform for a Aquamonix's cross-platform-ready iOS SCADA control app, designed from the ground up for future Android portability.

---

## Real-Time / Systems Bullets

* Implemented a multi-connection, multi-session task synchronization layer over WebSockets to maintain reliable state for long-running irrigation control jobs on a SCADA backend.

* Designed a WebSocket communication layer for persistent, bidirectional real-time control of industrial irrigation hardware via a Java middle tier.

---

## IoT / Industrial Bullets

* Developed mobile control software for industrial-scale SCADA irrigation systems — a domain requiring reliability guarantees well beyond typical consumer app expectations.

* Delivered the mobile interface layer for an Australian industrial IoT product, enabling operators to control large-scale irrigation infrastructure from a Xamarin iOS app.

---

# Strongest Resume Angles

## Mobile Architecture / Senior Mobile Roles

Emphasize:

* Greenfield build from scratch
* MVP architecture ownership
* Cross-platform portability planning
* Long-running task synchronization design
* WebSocket protocol layer

Strong signal for mobile engineering depth beyond typical feature-delivery work.

---

## IoT / Industrial / Embedded-Adjacent Roles

Emphasize:

* SCADA integration
* Industrial irrigation control
* Reliability requirements in physical infrastructure context
* Long-running task management
* Multi-connection state synchronization

Demonstrates ability to build mobile software where correctness has real-world physical consequences.

---

## Real-Time / Systems Engineering Roles

Emphasize:

* WebSocket communication layer
* Long-running task synchronization across sessions
* Multi-connection state management
* Java middle tier integration

Useful for roles requiring real-time data, persistent connections, or complex state management.

---

## Xamarin / Cross-Platform Mobile Roles

Emphasize:

* Xamarin iOS from scratch
* Cross-platform portability design
* C# and Objective-C interop
* Architecture designed for future platform expansion

---

# ATS / Keyword Bank

## Mobile / Platform Keywords

Xamarin, iOS, Objective-C, C#, cross-platform mobile, Xamarin iOS, mobile architecture, iOS SDK, mobile app development, greenfield mobile, MVP development.

## Real-Time / Protocol Keywords

WebSockets, real-time communication, bidirectional communication, persistent connections, long-running tasks, task synchronization, multi-session state, connection management.

## Industrial / IoT Keywords

SCADA, industrial automation, irrigation control, agricultural technology, IoT, industrial mobile app, physical infrastructure control, industrial IoT, supervisory control, data acquisition.

## Architecture Keywords

MVP architecture, cross-platform planning, portability design, architecture from scratch, greenfield architecture, system design, mobile-to-backend integration.

---

# External Claim Safety Notes

## Safe to Claim

* Built Aquamonix's Xamarin iOS app from scratch, 2015–2017
* App controlled large-scale SCADA irrigation systems via a Java middle tier
* Architected the MVP and designed cross-platform portability plan
* Implemented long-running task synchronization across multiple connections and app sessions
* Technologies: Xamarin, iOS, Objective-C, C#, WebSockets
* Client based in Australia

## Use With Care

* "Sole developer" framing — likely accurate given the from-scratch/MVP context, but exact team composition not stated; use "sole or lead developer" or "built from scratch" without overclaiming team absence
* "Architect" title — accurate to the work described but exact job title not confirmed

## Avoid Unless Confirmed

* Specific SCADA vendor or hardware platform (Rockwell, Siemens, Schneider, etc.)
* Number of irrigation sites or scale of deployments
* Whether the app reached production / was commercially deployed
* Specific irrigation command types or protocols used
* Whether the cross-platform port was ever executed

---

# Missing / Worth Clarifying

1. Exact job title during this engagement.
2. Were you the sole developer, or were there others on the iOS/mobile side?
3. Was this freelance/consulting or a full-time role?
4. Which SCADA platform or hardware did Aquamonix's system use?
5. Was the app deployed to the App Store or used internally/by clients directly?
6. Did the cross-platform port (Android or others) ever get executed, and did you contribute to it?
7. Specific nature of the long-running tasks: irrigation schedules, zone activation, valve control, etc.?
8. What was the Java middle tier — a custom server, a vendor platform, or an existing Aquamonix backend?
9. How were WebSocket reconnects and offline states handled?
10. Was this a consulting engagement or direct employment with Aquamonix?
