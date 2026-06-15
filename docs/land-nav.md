# Land navigation & terrain

> **Disclaimer:** Educational / reference / preparedness material with links to public and open-source resources. Not operational instructions for violence or weapons. Verify against primary sources; train with qualified instructors. Follow all applicable laws.

Land navigation and terrain analysis is the systematic practice of determining your position, planning routes, and moving through terrain using maps, compasses, coordinate systems, and natural features. Taught across military, emergency services, search-and-rescue, and civilian outdoors communities, core skills include map reading (topographic interpretation, contour lines, terrain features), coordinate systems (MGRS, UTM, lat/lon), compass work (declination correction, azimuths, resection), distance measurement (pace count), terrain association, and the analytical frameworks OAKOC/KOCOA (terrain analysis) and METT-TC (mission planning variables). The authoritative military reference is TC 3-25.26 (formerly FM 3-25.26), a public-release US Army training circular. GPS technology supplements but does not replace foundational map-and-compass skills, which remain essential when electronics fail.

## Maps and Map Reading Fundamentals

A topographic map is a two-dimensional representation of three-dimensional terrain using contour lines, symbols, and a standardized legend. Key map elements include: scale (e.g., 1:25,000 means 1 unit on map = 25,000 units on ground); a legend/marginal information explaining symbols; a north arrow showing true north, magnetic north, and grid north; a contour interval (the elevation difference between adjacent contour lines); and a bar scale for measuring distances.

Contour lines connect points of equal elevation. Rules that always hold: (1) Every point on a contour line is the same elevation. (2) Contour lines never cross or merge (except at a vertical cliff). (3) Closely spaced lines = steep terrain; widely spaced lines = gentle slope. (4) Index contours (every 5th line, printed bolder with an elevation label) provide quick reference. (5) Contour lines pointing uphill in a V or U shape indicate a drainage (stream valley); pointing downhill indicate a ridge or spur.

Map colors follow a standard scheme: green = vegetation; blue = water; brown = contour/topography; black = man-made features; red = major roads and boundaries; white = open ground (no vegetation).

The standard US military/USGS scale for foot navigation is 1:25,000. USGS 7.5-minute quadrangle sheets (1:24,000) are the equivalent civilian standard. All USGS topos are freely downloadable as public-domain PDFs and GeoPDFs from the National Map (apps.nationalmap.gov/downloader).

## Coordinate Systems: MGRS, UTM, and Lat/Long

Three coordinate systems are most relevant for field navigation:

**WGS84 Latitude/Longitude** is the global standard used by GPS receivers and Google Maps. Expressed in degrees, minutes, seconds (DMS) or decimal degrees (DD). The datum WGS84 (World Geodetic System 1984) is maintained by the US National Geospatial-Intelligence Agency and is what all modern GPS devices reference.

**UTM (Universal Transverse Mercator)** divides the Earth into 60 north-south zones, each 6 degrees wide, numbered 1-60 west to east. Within each zone, positions are given as an Easting (meters east of the zone's central meridian, false origin 500,000m) and Northing (meters north of the equator, or for southern hemisphere, a false origin of 10,000,000m south). UTM is ideal for metric distance calculation and direct comparison: 1,000m = 1km on the ground regardless of latitude.

**MGRS (Military Grid Reference System)** builds on UTM by adding a two-letter 100,000-meter square identifier within each zone, then appending numeric easting/northing to the desired precision. A full MGRS coordinate looks like: 18S UJ 12345 67890. Reading left to right: '18S' = Grid Zone Designation (GZD); 'UJ' = 100km square ID (letters I and O are never used to avoid confusion with 1 and 0); '12345 67890' = 5-digit easting and northing, giving 1-meter precision (10-digit total). A 4-digit grid (2+2) gives 1,000m precision; 6-digit gives 100m; 8-digit gives 10m; 10-digit gives 1m. Mnemonic for reading: 'along the corridor (easting), then up the stairs (northing)' — always read easting first, then northing. MGRS letters avoid ambiguity in radio voice communication and are the standard for US and NATO military operations.

## Compass Use and Magnetic Declination

A compass aligns with Earth's magnetic field, which does not coincide with geographic (true) north. The angular difference is called **magnetic declination** (also called magnetic variation). It varies by location and changes slowly over time — typically 0-25 degrees in the continental US, and as much as 30+ degrees in Alaska. Declination can be East (compass needle deflected east of true north, meaning your magnetic bearing is LESS than true) or West (compass needle deflected west, meaning your magnetic bearing is MORE than true). Topo maps print a declination diagram in the margin; always check the map's revision date and verify against NOAA's current calculator (ngdc.noaa.gov/geomag/declination.shtml) since declination drifts.

Conversion rules: if declination is EAST, subtract it from magnetic bearing to get true bearing (or add it to get magnetic from true). If declination is WEST, add it to magnetic bearing to get true (or subtract from magnetic). Memory aid: 'East is least (subtract); West is best (add)' converts magnetic to true.

**The lensatic compass** (standard US military issue) has a sighting wire and lens system for precise azimuth shooting. The compass-to-cheek method: open cover 90 degrees, eyepiece at 45 degrees, align sighting wire with target through lens, read azimuth off the drum. The center-hold method is faster for general navigation. Military compasses use mils (6,400 mils in a circle) as well as degrees; civilian orienteering compasses use degrees only.

**Shooting an azimuth:** Face your target, hold compass level, align sighting wire, read bearing (0-360 degrees). Walk that bearing to the target.

**Resection (finding your position):** Identify two or more known landmarks visible from your position and on your map. Shoot an azimuth to each. Calculate the back-azimuth for each (add or subtract 180 degrees). Draw lines on the map through each landmark at its back-azimuth. Where the lines intersect is your location. Three landmarks gives a triangle of error; your position is inside it.

**Back-azimuth:** If azimuth < 180, add 180. If azimuth >= 180, subtract 180. In mils: add or subtract 3,200.

## Pace Count and Distance Measurement

Pace count is the primary non-electronic method for measuring ground distance traveled. A pace is one natural step — two steps equals one pace (left-foot-strike to left-foot-strike). The goal is to know your personal pace count for 100 meters.

**Calibration procedure:** Measure a 100-meter course on terrain similar to your operational environment. Walk it at least three times carrying your usual gear load. Count left-foot strikes. Average the three runs. That average is your baseline pace count. Most adults fall between 62 and 75 paces per 100 meters under field conditions; taller individuals tend toward the low end.

**Adjustment factors** (all increase your pace count): uphill travel (expect +10-20 paces per 100m on steep slopes); night or low visibility; dense vegetation; mud, snow, or wet ground; heavy pack; physical exhaustion. The flat-terrain calibration is your minimum; real conditions only raise the number.

**Ranger beads (pace count beads):** A cord with two groups of beads — 9 lower beads representing 100m increments, 4 upper beads representing 1km increments (each upper bead = all 9 lower beads cycled once). Total capacity: 5km before reset. Operation: each time you complete your personal 100m pace count, slide one lower bead. After 9 lower beads (900m), the next 100m completes 1km — move one upper bead, reset lower beads. Reset when entering new leg or at checkpoints.

**Converting pace to distance:** Distance (m) = (your pace count per 100m) x (desired meters / 100). Example at 68 paces/100m, to travel 350m: (68 x 3) + (68 x 0.5) = 204 + 34 = 238 paces.

**Alternative methods:** map measurement with a roamer (grid scale tool on baseplate compass), map wheel, or string laid along the route then measured against the bar scale. GPS devices give direct distance readout but require batteries.

## Terrain Features and Terrain Association

Terrain association is matching what you observe on the ground to what you see on the map, and vice versa. It is generally considered the most practical land navigation skill for continuous movement because it does not require precise compass bearings on every leg.

**Five major terrain features** (the backbone of map reading):
1. Hill — a point or small area of high ground; ground slopes down in all directions from the summit. Contour signature: nested closed loops, smallest at top.
2. Ridge — a line of high ground with height variations along its crest; you can walk along it with ground falling away on both sides. Contour signature: U or V shapes pointing away from high ground.
3. Valley — a groove or depression in the land, usually formed by stream erosion; a stream usually runs through it. Contour signature: U or V shapes pointing toward high ground (up-valley).
4. Saddle — a dip or low point between two hills along a ridge line; not necessarily a pass. Contour signature: an hourglass-shaped gap between two hilltop loops.
5. Depression — a low point or hole surrounded on all sides by higher ground. Contour signature: closed loop with tick marks (hachure marks) pointing inward.

**Three minor terrain features:**
1. Draw — a less developed stream course, smaller than a valley; water collects here after rain. Contour signature: minor V pointing uphill.
2. Spur — a short, continuous sloping line of higher ground coming out from a hill or ridge. Contour signature: minor U pointing downhill.
3. Cliff — a vertical or near-vertical slope; may appear as contour lines touching or very nearly touching.

**Two supplementary terrain features:**
- Cut: man-made removal of high ground for road/railway construction.
- Fill: man-made deposit of low ground.

**Terrain association technique:** Orient your map to north (compass or by line-up with a feature). Identify your general area. Pick two or three distinctive nearby features (hilltop, road junction, stream bend) visible on both map and ground. Confirm they match. As you move, continuously update your estimated position using visible features. Deliberate offset navigation: if your objective is near a linear feature (road, river, ridge), aim intentionally to one side so you know which direction to turn when you hit the linear feature — eliminates the uncertainty of 'which way do I go?'

## OAKOC / KOCOA Terrain Analysis

OAKOC (also written KOCOA or OCOKA — same five factors in different order) is the military doctrinal framework for analyzing terrain in support of tactical planning. It is described in FM 6-0 and ATP 2-01.3 and forms part of the Intelligence Preparation of the Battlefield (IPB) process. OAKOC is taught as doctrine at the US Army Infantry School (Fort Moore) and the Marine Corps TBS. It is descriptive and analytical — it describes how to think about terrain, not how to conduct combat operations.

The five factors:

**O — Observation and Fields of Fire:** What can be seen from a given position, and what can be engaged with direct fire weapons? Considers line of sight, vegetation masking, terrain masking, and dead ground (terrain not visible from a firing position). For navigation purposes: elevated ground often offers observation to confirm terrain association; dead ground can conceal movement.

**A — Avenues of Approach:** Routes by which a force can move toward an objective or away from an area. Avenues are assessed for width (can the required force fit?), surface condition, slope, and obstacles. For civilian navigation: avenues are simply practical route corridors — valleys, roads, ridgelines used as travel lanes.

**K — Key and Decisive Terrain:** Ground whose occupation or control provides a marked advantage. Classic examples: a hilltop with observation over surrounding lowland; a bridge over an otherwise uncrossable waterway; a chokepoint in a valley. For navigation planning: key terrain often makes the best navigation checkpoints because it is unambiguous on map and ground.

**O — Obstacles:** Natural or man-made features that stop, slow, or channel movement. Natural obstacles include rivers, swamps, cliffs, dense vegetation. Man-made include walls, wire, ditches, minefields. For civilian navigation: identifying obstacles in advance prevents route failures.

**C — Cover and Concealment:** Cover provides protection from direct-fire weapons (earthen berms, masonry walls, large trees). Concealment hides from observation but does not stop projectiles (brush, shadows, smoke). For navigation: dense vegetation shown on a map may indicate slow movement and poor visibility, affecting time estimates.

METT-TC context: OAKOC is the terrain-analysis sub-tool within the 'T' (Terrain and Weather) variable of the METT-TC planning framework. The full METT-TC variables are: Mission, Enemy, Terrain and Weather, Troops and Support Available, Time Available, Civil Considerations. Weather is sometimes analyzed separately as BMPT (Battlefield Weather): Visibility, Wind, Precipitation, Temperature/humidity, affecting movement rates, navigation technique selection (GPS vs map, day vs night navigation), and ground conditions.

## GPS Basics for Field Navigation

GPS (Global Positioning System) is a US Department of Defense satellite constellation providing position, navigation, and timing (PNT) data worldwide. As of 2000, Selective Availability (intentional civilian accuracy degradation) was permanently disabled; civilian receivers now achieve the same signal quality as military non-encrypted receivers: approximately 3-10 meters accuracy. WAAS (Wide Area Augmentation System, operated by the FAA) uses ground reference stations to correct satellite errors, improving accuracy to 1-3 meters for WAAS-enabled receivers within CONUS coverage.

**Datum:** All modern GPS receivers default to WGS84. Topo maps may use NAD27 or NAD83 as their datum. Always confirm your GPS datum matches your map datum before use; a datum mismatch can introduce 100-300 meter position errors.

**Display modes relevant to land nav:** Most GPS units can display in lat/long (decimal degrees or DMS), UTM, or MGRS — set to match your map. MGRS is the standard for military operations and many SAR teams.

**GPS limitations:** Requires battery power (always carry spares or a backup power bank). Signal can be degraded in deep canyons, dense forest canopy, or under heavy cloud/weather. Initial fix from cold start can take 1-5 minutes. Electronics can fail from water, impact, or EMP. GPS tells you where you are, not what the terrain looks like — it does not replace map reading skill.

**Recommended civilian GPS practices:** (1) Pre-load waypoints and route from desktop software (CalTopo, Gaia GPS) before entering the field. (2) Download offline map tiles for your operational area. (3) Carry a printed topo map and compass as backup — never rely solely on a single electronic device. (4) Mark your trailhead/vehicle as a waypoint immediately upon arrival. (5) Record a track log to enable backtracking.

**Open tools:** CalTopo (caltopo.com) is the leading free/freemium web tool for pre-mission mapping, supporting USGS topos, slope angle shading, MGRS grids, and printable maps. Gaia GPS (gaiagps.com) is the companion mobile app. OsmAnd (osmand.net) is a fully open-source offline navigation app using OpenStreetMap data, available on Android and iOS at no cost.

## Navigation Planning: Dead Reckoning, Route Selection, and Common Errors

**Dead reckoning** is the process of computing your current position from a known starting point by tracking direction and distance traveled. It combines compass azimuth (direction) with pace count (distance). For each leg: face the desired azimuth, count paces until target distance is reached, then update your position on the map. Dead reckoning accumulates error over distance; terrain association should be used to check and correct position at known features.

**Route planning steps:** (1) Study the map for the entire route before moving. (2) Identify checkpoints — unmistakable terrain features at intermediate points along the route. (3) Break the route into legs connecting checkpoints, each with a compass azimuth and estimated distance. (4) Note significant obstacles along each leg. (5) Identify attack points — obvious terrain features close to the final objective from which you can make a precise final approach. (6) Estimate travel time using terrain-adjusted speed: open flat terrain ~4km/hr foot speed; mixed terrain ~2-3km/hr; dense vegetation or steep slopes ~1-2km/hr. Add stops and time for navigation checks.

**Deliberate offset:** When the destination is near a linear feature (road, river, fence), deliberately aim 200-300m to one known side. When you hit the linear feature, you know which direction to turn — eliminates the 50-50 guessing problem of straight-ahead dead reckoning.

**Common navigation errors:** (1) Failure to correct for magnetic declination — results in cumulative directional error. (2) Using the wrong datum on GPS vs. map. (3) Trusting pace count from flat calibration on hilly terrain — always add margin. (4) Poor map orientation — always orient the map to north before analysis. (5) Terrain feature misidentification — multiple hills or saddles can look similar; verify with a second feature. (6) Not updating position at every checkpoint — 'staying found' requires continuous updates, not just fixing position when lost. The best navigators rarely get lost because they never allow themselves to become uncertain of their position for more than a few hundred meters.

### Checklist: Pre-Mission Map Preparation

- [ ] Obtain the correct map sheet(s) covering your entire route plus buffer
- [ ] Check the map's edition date and datum (NAD27, NAD83, or WGS84)
- [ ] Note the contour interval and bar scale in the map margin
- [ ] Read the declination diagram: record the G-M angle (grid to magnetic) and the date
- [ ] Verify current declination at NOAA calculator (ngdc.noaa.gov/geomag) if map is old
- [ ] Mark your start point, objective, checkpoints, and attack point in pencil
- [ ] Draw route legs and record the azimuth and distance for each leg
- [ ] Identify key terrain features and obstacles along each leg
- [ ] Note any avenues of approach and deliberate offset direction near the objective
- [ ] Cover or laminate the map if wet conditions are expected

### Checklist: Navigation Kit Checklist

- [ ] Topographic map of the area (1:25,000 or 1:24,000 preferred)
- [ ] Compass (lensatic or baseplate, with a working declination setting)
- [ ] Protractor or roamer matching your map scale
- [ ] Pencil and waterproof notebook for recording legs, pace counts, observations
- [ ] Ranger beads (pace count beads) or wrist counter
- [ ] GPS device or smartphone with offline maps downloaded (CalTopo/Gaia GPS)
- [ ] Spare batteries or backup power for electronics
- [ ] Printed paper map as backup even if using GPS
- [ ] Signal device (whistle, mirror, PLB) for emergency use
- [ ] Red-lens flashlight or headlamp for night navigation

### Checklist: Compass-to-Cheek Azimuth Procedure (Lensatic Compass)

- [ ] Open the compass cover to approximately 90 degrees from the base
- [ ] Set the eyepiece (rear sight) to approximately 45 degrees
- [ ] Hold the compass at eye level with the sighting wire aligned toward the target
- [ ] Look through the eyepiece lens and align the sighting wire with your target
- [ ] While maintaining alignment, read the bearing from the rotating drum beneath the index line
- [ ] Note the azimuth; if using magnetic bearing on a map with declination, convert as required
- [ ] Verify by repeating the sighting — minor variations are normal; average three readings for precision

### Checklist: Resection (Finding Your Position with a Compass and Map)

- [ ] Identify two or more distinct landmarks visible on the ground AND on your map
- [ ] Shoot an azimuth to Landmark 1; record the magnetic azimuth
- [ ] Calculate back-azimuth (if < 180, add 180; if >= 180, subtract 180)
- [ ] Draw a line on the map through Landmark 1's map symbol at the back-azimuth angle
- [ ] Repeat for Landmark 2 (and ideally Landmark 3)
- [ ] The point where the lines intersect is your position
- [ ] With three lines, your position is inside the triangle of error; pick the centroid
- [ ] Confirm by checking nearby terrain features match your estimated position

### Checklist: Pace Count Calibration Procedure

- [ ] Measure a 100-meter baseline on ground representative of your mission terrain
- [ ] Put on the load you will carry in the field
- [ ] Start with feet together; step off on left foot
- [ ] Count each time the LEFT foot strikes the ground (one pace = two steps)
- [ ] Walk the baseline three times; record each count
- [ ] Average the three runs — this is your 100m pace count
- [ ] Add 10-20 paces for steep uphill legs; increase for night, mud, snow, or heavy vegetation
- [ ] Verify pace count against known distances at checkpoints during the mission

### Checklist: OAKOC Terrain Analysis Checklist

- [ ] O — Observation: What can be seen from key positions? Identify dead ground and masking terrain
- [ ] A — Avenues of Approach: What corridors allow movement toward the objective? Grade, width, surface?
- [ ] K — Key Terrain: What ground provides decisive advantage if controlled? Hilltops, bridges, chokepoints?
- [ ] O — Obstacles: What stops or channels movement? Rivers, cliffs, dense vegetation, man-made barriers?
- [ ] C — Cover and Concealment: What provides protection (cover) or hides movement (concealment)?
- [ ] Assess how each factor affects YOUR movement
- [ ] Assess how each factor affects any opposing force or hazard
- [ ] Integrate weather effects (visibility, ground conditions) into each factor

## Resources & links

- [TC 3-25.26 Map Reading and Land Navigation (Part 1 PDF) — Army Writer](https://www.armywriter.com/board/references/TC3-25x26-Part1.pdf) — Direct PDF of the current US Army Training Circular (Nov 2013); public release; the authoritative reference for all Army land navigation doctrine
- [FM 3-25.26 Map Reading and Land Navigation — Internet Archive](https://archive.org/details/FM3-25x26) — Free download of the earlier Field Manual version; public domain; predecessor to TC 3-25.26; content largely the same
- [NOAA Magnetic Declination Calculator — NCEI/NGDC](https://www.ngdc.noaa.gov/geomag/declination.shtml) — Authoritative government tool for current magnetic declination at any location worldwide; uses World Magnetic Model (WMM)
- [USGS National Map Downloader — Free Topo Maps](https://apps.nationalmap.gov/downloader/) — Free download of current and historical USGS topographic maps (GeoPDF, GeoTIFF) for any US location; public domain
- [CalTopo — Backcountry Mapping and Route Planning](https://caltopo.com) — Free/freemium web tool for pre-mission mapping; supports USGS topos, MGRS grid overlays, slope angle shading, and printable custom maps
- [Gaia GPS — Offline Navigation App](https://www.gaiagps.com) — Mobile GPS app (iOS/Android) with offline topo maps; free tier available; integrates with CalTopo for pre-planned routes
- [OsmAnd — Free Open-Source Offline Navigation](https://osmand.net) — Fully open-source offline navigation app using OpenStreetMap data; free on F-Droid; no account required; supports UTM/MGRS display
- [MGRS Coordinate Converter — MapScaping](https://mapscaping.com/mgrs-coordinate-converter/) — Free online converter between MGRS, lat/long, and UTM; interactive map display; no signup required
- [ITS Tactical: Complete Guide to Land Navigation with MGRS](https://www.itstactical.com/skillcom/navigation/the-complete-guide-to-land-navigation-with-the-military-grid-reference-system/) — Detailed civilian-written step-by-step guide to MGRS: grid zones, 100k squares, reading 8- and 10-digit coordinates, practical field tips
- [ITS Tactical: Understanding UTM](https://www.itstactical.com/skillcom/navigation/landnav-101-understanding-the-universal-transverse-mercator-system-utm/) — UTM system explained: zones, eastings, northings, relationship to MGRS; good primer before learning MGRS
- [REI Expert Advice: How to Adjust Compass Declination](https://www.rei.com/learn/expert-advice/compass-declination.html) — Civilian-oriented guide to declination: what it is, east vs west, how to set adjustable compasses, conversion rules
- [Gray Bearded Green Beret: Pace Count and Ranger Beads](https://graybeardedgreenberet.com/blogs/the-gray-bearded-green-beret-blog/determining-distance-pace-count-and-ranger-beads) — Practical guide with typical pace count values (62-75 per 100m), ranger bead construction and use, terrain adjustment factors
- [Land-Navigation.com: Terrain Association](https://www.land-navigation.com/terrain-association.html) — Dedicated civilian site explaining terrain association technique including Google Earth armchair practice method
- [Army Study Guide: Major and Minor Terrain Features](https://www.armystudyguide.com/content/Prep_For_Basic_Training/prep_for_basic_common_tasks/identify-terrain-features.shtml) — Quick-reference definitions of the five major (hill, ridge, valley, saddle, depression) and three minor (draw, spur, cliff) terrain features with contour descriptions
- [USMC TBS Lensatic Compass Student Handout (PDF)](https://www.trngcmd.marines.mil/Portals/207/Docs/TBS/B182056%20Lensatic%20Compass.pdf) — Official USMC Training and Education Command handout on lensatic compass use; public release; covers compass-to-cheek method, azimuths, back-azimuths
- [Wikipedia: Military Grid Reference System](https://en.wikipedia.org/wiki/Military_Grid_Reference_System) — Well-maintained encyclopedia article on MGRS; covers GZD structure, 100k squares, precision levels, relationship to UTM
- [AskTOP.net: FM 3-25.26 Historical Download](https://asktop.net/army-downloads/references/field-manuals/fm-3-25-26-map-reading-and-land-navigation-historical-copy-superseded-by-tc-3-25-26-map-reading-and-land-navigation/) — Hosted download of the superseded FM 3-25.26 for historical reference; same core content as TC 3-25.26 for most land nav topics
- [Gaia GPS: How to Read Topographic Maps](https://blog.gaiagps.com/how-to-read-topographic-maps/) — Accessible civilian introduction to topo map reading: contour lines, index contours, valley vs ridge signatures, scale, and using digital topos
