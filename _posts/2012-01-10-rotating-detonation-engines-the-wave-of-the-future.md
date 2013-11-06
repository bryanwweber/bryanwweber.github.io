---
layout: post
title: ! 'Rotating Detonation Engines: the "wave" of the future?'
categories:
- Articles
tags:
- engine
- jet engine
- propulsion
- pulsed detonation engine
- rocket
- rotating detonation wave
---
The desire for energy security and (lack of) climate change are driving two avenues of innovation to power the next generation of vehicles. The first avenue is to invent new fuels, such as bio-fuels, that change the supply dynamics of the industry. The second avenue is to invent entirely new engine concepts to improve efficiency. One such concept, using [detonations](http://en.wikipedia.org/wiki/Detonation) (as opposed to [deflagrations](http://en.wikipedia.org/wiki/Deflagration)) to combust fuel and air mixtures, has been investigated since [the 1940's](http://ronney.usc.edu/AME514S11/Lecture13/Papers/KailasPDEreview-AIAAJ2000.pdf). Using detonations allows for much higher efficiency engine operation. One of the most common types of detonation engines is the Pulsed Detonation Engine (PDE). Unfortunately, due to many difficulties including the intermittent nature of thrust from such engines, no PDEs have been commercially produced to date (although the concept has flown in an [Air Force test plane][testplane]).
<!--more-->

In a recent review paper, Kailasanath has discussed the history and current work on a similar detonation engine concept, called a Rotating Detonation Engine (RDE). An RDE is a similar concept to a PDE in that it uses detonation to burn the fuel and air, but the RDE offers some advantages over the PDE, primarily that the detonation is continuous in an RDE. This means that an RDE can generate thrust continuously instead of intermittently. In addition, the continuous operation of an RDE allows it to have higher efficiency than a PDE.

A typical PDE is not much more complex than a cylinder containing a combustion chamber, into which fuel and air are fed, an ignitor and a nozzle to generate thrust. The fuel and air are pulsed into the combustion chamber, ignited into a detonation, and expanded through the nozzle, with the detonation travelling along the long axis of the cylinder. An RDE, by contrast, is more complex. A typical RDE configuration is a ring-shaped cylinder, where fuel is fed from one end of the cylinder and a nozzle is at the other end of the cylinder. The detonation wave travels tangentially around the cylinder, burning the fuel and air as they are fed into the ring. At the other end of the chamber, the gases are expanded through the nozzle to generate thrust. This is different from a PDE, where the detonation wave travels from the front of the cylinder to the back along the long axis, while in the RDE the detonation wave travels circumferentially around the cylinder. The following pair of images shows the difference between the operation of each type of engine. It is important to note that the Rotating or Pulsed indicates the nature of the combustion wave - not the rotation of parts in the engine.

{:.centerimg}
![Example schematic of a Pulsed Detonation Engine. Source: UCLA Energy and Propulsion Research Laboratory]({{ site.baseurl }}/files/2012/01/engine_schematic2.jpg) <br /> Example Schematic of a Pulse Detonation Engine. Source: [UCLA Energy and Propulsion Research Laboratory](http://www.seas.ucla.edu/combustion/projects/pulsed_detonation_wave.html)
![Example schematic of a Rotating Detonation Engine. Source: Kailasanath]({{ site.baseurl }}/files/2012/01/Kailasanath_RDE.png) <br /> Example schematic of a Rotating Detonation Engine. Source: Kailasanath

According to Kailasanath, research into RDE's began in the late 1950's and early 1960's, and focused primarily on application of RDE's to rocket propulsion. More recent research has extended the usefulness of RDE's to air-breathing propulsion (i.e. jet-engine-like propulsion). In addition to this experimental work, other recent work has focused on modeling RDE's using computer code. These computer simulations have been used to investigate the overall flow field in an RDE as well as the performance of an RDE as various engine operating parameters are varied.

Two of the primary control parameters available to experimenters (and the parameters that are varied in the simulations mentioned above) are the pressure of the fuel and the air at the inlet, and the pressure at the nozzle end of the engine, called the inlet pressure and back pressure respectively. Because of the conditions in the combustion chamber of a detonation engine, the mass flow rate of the fuel and air mixture through the engine depends only on the inlet pressure (and not on the back pressure), but the thrust of the engine depends on both parameters. Interestingly, the [specific impulse][isp] (a measure of the efficiency of the engine) depends only on the ratio of the inlet and back pressures, but not on specific values of either parameter. The maximum value of specific impulse achieved in this study was about 33% higher than a comparable PDE, confirming the advantages that RDE's should have over PDE's. The author concludes by noting that the value of specific impulse computed in their study is quite close to the theoretical ideal efficiency, and further optimizations of the engine may allow the RDE to get even closer to the theoretical maximum.

Citation: K. Kailasanath, "The Rotating-Detonation-Wave Engine Concept : A Brief Status report," 49th AIAA Aerospace Sciences Meeting, 2011, Paper AIAA-2011-0580.

[isp]: http://www.grc.nasa.gov/WWW/k-12/airplane/specimp.html
[testplane]: http://www.afmc.af.mil/news/story_print.asp?id=123098900
