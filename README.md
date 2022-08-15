# Lyft Rental Fleet Service
Lyft is in the process of rolling out a new rental fleet in the hopes of encouraging more connected, sustainable cities across the US. The component is responsible for determining whether cars in Lyft’s new rental fleet should be serviced when they are returned. Whether or not a car should be serviced depends on two factors at the moment - the engine and battery. There are five car models in Lyft’s fleet, each with a different engine-battery combination. Each of the three types of engines has its own criteria for determining when it should be serviced. The same applies to each type of battery. These service criteria will change somewhat frequently in the future, and new car models are bound to be added to the fleet. 

The component is extensible and easy to modify, so new service criteria can be added quickly and efficiently. 

The current service criteria are as follows:

Engines
- Capulet Engine - should be serviced once every 30,000 miles
- Willoughby Engine - should be serviced once every 60,000 miles
- Sternman Engine - should be serviced only when the warning indicator is on
- Batteries
- Spindler Battery - should be serviced once every 2 years
- Nubbin Battery - should be serviced once every 4 years

The current car models are as follows:

- Calliope
  - Capulet Engine
  - Spindler Battery
- Glissade
  - Willoughby Engine
  - Spindler Battery
- Palindrome
  - Sternman Engine
  - Spindler Battery
- Rorschach
  - Willoughby Engine
  - Nubbin Battery
- Thovex
  - Capulet Engine
  - Nubbin Battery
