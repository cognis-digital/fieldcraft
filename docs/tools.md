# Open-source tools

> **Disclaimer:** Educational / reference / preparedness material with links to public and open-source resources. Not operational instructions for violence or weapons. Verify against primary sources; train with qualified instructors. Follow all applicable laws.

A curated field reference for open-source and freely available tools covering offline mapping, navigation, radio communications, first-aid/medical reference, and offline knowledge access — oriented toward preparedness, emergency response, and field operations. All tools listed are publicly available; no credentials, special clearances, or paid tiers are required for the core functionality described. Primary audiences include first responders, emergency managers, backcountry travelers, ham radio operators, and anyone building resilient off-grid capability.

## Offline Mapping: QGIS, QField, and the Desktop GIS Stack

QGIS (https://qgis.org) is the dominant open-source desktop GIS platform, roughly equivalent in capability to Esri ArcGIS but fully free under the GNU GPL. It handles vector and raster data, plugins for hundreds of workflows, and can export tile packages for offline field use. For mobile field data collection, QField (https://qfield.org, GitHub: https://github.com/opengisch/QField) is QGIS's official companion app — it reads QGIS project files, supports fully offline vector and raster editing, rich survey forms, photo/audio attachment, and external GNSS receivers. Changes sync back to the QGIS desktop project. Mergin Maps (https://merginmaps.com) is another QGIS-based sync platform with a self-hostable server option. To prepare offline basemap tiles before going into the field, QTiles 2 (QGIS plugin) renders a tile pyramid from any QGIS project and exports it as MBTiles or a directory. NextGIS Data Tiles provides pre-built basemaps downloadable for offline use. QGIS runs on Windows, macOS, and Linux.

## Mobile Offline Navigation: OsmAnd, Organic Maps, and OpenStreetMap

OpenStreetMap (OSM, https://www.openstreetmap.org) is the foundational community-maintained map database underlying most open-source navigation tools. It is freely licensed (ODbL) and editable by anyone with an account.

OsmAnd (https://osmand.net, GitHub: https://github.com/osmandapp/OsmAnd) is a full-featured offline navigation app for Android and iOS. It stores complete country or regional map packs on-device, provides turn-by-turn voice guidance for driving, cycling, and hiking, displays topographic contours, supports external GPS receivers, and allows GPX track import/export. The full-featured ad-free build is available from F-Droid (https://f-droid.org/packages/net.osmand.plus/) as OsmAnd~, with no Google dependencies — important for privacy-sensitive or de-Googled devices.

Organic Maps (https://organicmaps.app) is a lighter, cleaner alternative by the original Maps.me founders. It has no ads, no trackers, excellent hiking/trail detail from OSM, and supports unlimited offline country downloads for free. Recommended for casual field navigation where OsmAnd's depth is not needed.

Both apps support importing custom GPX waypoints and tracks, which is the standard exchange format compatible with GPSBabel and most GPS hardware.

## Situational Awareness: ATAK / CivTAK and the TAK Ecosystem

ATAK (Android Team Awareness Kit / Android Tactical Assault Kit depending on context) is a geospatial situational awareness and collaboration platform originally developed by the U.S. Air Force Research Laboratory and now maintained by the DoD's TAK Product Center. The civilian version, ATAK-CIV (also called CivTAK), was open-sourced in 2020. The source code is on GitHub at https://github.com/deptofdefense/AndroidTacticalAssaultKit-CIV. The app can be downloaded from Google Play or the TAK Product Center (tak.gov).

Core capabilities: real-time shared map with blue-force tracking (showing team member positions), chat, file/image sharing, offline map layers, elevation analysis, drawing/markup tools, medevac forms, and plugin architecture. It uses the Cursor on Target (CoT) XML/Protobuf protocol over UDP/TCP/TLS for device-to-device or device-to-server messaging.

The broader TAK ecosystem includes:
- WinTAK (Windows desktop client)
- iTAK (iOS client)
- TAK Server (official, recently open-sourced): the reference server for routing CoT messages
- OpenTAKServer (https://github.com/brian7704/OpenTAKServer): community open-source TAK server, runs on Raspberry Pi, supports ATAK/WinTAK/iTAK clients, documented at https://docs.opentakserver.io
- FreeTakServer (https://github.com/FreeTAKTeam/FreeTakServer): Python-based, has REST API and Node-RED integration

Use cases beyond military: wildland fire, search and rescue, disaster response, law enforcement, and coordinated expedition teams. Teams can operate fully peer-to-peer over Wi-Fi or via a server over LAN, internet, or satellite. CivTAK community hub: https://www.civtak.org

## Off-Grid Radio: CHIRP, GQRX / GNU Radio, and Meshtastic

Three distinct tool families cover radio for field preparedness:

1. CHIRP (https://chirp.danplanet.com): Free, open-source, cross-platform (Windows/macOS/Linux) programming software for two-way radios. Supports hundreds of radios — Baofeng, Yaesu, Icom, Kenwood, Wouxun, Retevis, and many more. Lets you program memory channels, frequencies, CTCSS/DCS tones, and offsets, and import frequency lists from online repositories (e.g., RadioReference). Released under GNU GPL. Written and maintained since 2008 by Dan Smith KK7DS and volunteers. Essential tool before any deployment: load local repeaters, NOAA weather channels, GMRS/FRS calling channels, and simplex emergency channels.

2. GQRX (https://www.gqrx.dk, GitHub: https://github.com/gqrx-sdr/gqrx): Open-source SDR receiver GUI powered by GNU Radio and Qt. Supports RTL-SDR dongles ($10-25 hardware), HackRF, Airspy, BladeRF, USRP, and any SoapySDR-compatible device. Demodulates AM, FM, SSB, CW; shows FFT spectrum and waterfall display; records audio and raw IQ. Licensed GNU GPL. Also see GNU Radio (https://www.gnuradio.org) for programmable signal processing chains. RTL-SDR.com (https://www.rtl-sdr.com) is the community hub for RTL-SDR tutorials, scanner software, and open-source tools.

3. Meshtastic (https://meshtastic.org, GitHub: https://github.com/meshtastic/firmware): Open-source firmware for LoRa-based mesh radio hardware. Turns $20-60 ESP32/nRF52 LoRa boards (Heltec, RAK, LilyGO T-Beam) into a license-free, encrypted text-messaging mesh network requiring no infrastructure. Each node rebroadcasts, extending range across the team. Documented range of 331 km in optimal conditions; typical urban/suburban range 1-5 km per hop. Uses AES256 encryption. Controlled via Android/iOS app or CLI. No FCC license required in ISM bands (915 MHz in North America). Excellent for SAR teams, backcountry parties, and comms in infrastructure-degraded environments.

## GPS Data Management: GPSBabel

GPSBabel (https://www.gpsbabel.org, GitHub: https://github.com/GPSBabel/gpsbabel) is the universal GPS data conversion and transfer utility. It converts waypoints, tracks, and routes among approximately 100 formats — Garmin serial and USB, Magellan, DeLorme, National Geographic TOPO!, GPX (the standard interchange format), KML/KMZ, CSV, and many more. It can also directly upload/download data to Garmin and Magellan devices connected by USB or serial.

Key field uses: extract waypoints from one device format and load them to another; convert a KML file from Google Earth into GPX for OsmAnd or QGIS import; batch-export tracks from a GPS receiver after a patrol or expedition; convert between coordinate systems. GPSBabel has both a command-line interface and a cross-platform GUI (GPSBabelFE). It is part of standard Debian/Ubuntu/Fedora Linux repositories and available on Homebrew for macOS. Licensed GPL. Initial release 2002; actively maintained.

## Offline Knowledge: Kiwix, Field Manuals, and Reference Archives

When internet access is unavailable, pre-downloaded knowledge becomes critical.

Kiwix (https://kiwix.org): Open-source offline browser that reads ZIM archive files — highly compressed, fully indexed snapshots of websites including Wikipedia (full text + images, ~100 GB for English), Wiktionary, WikiHow, Project Gutenberg, Stack Overflow, and many more. Available as a desktop app (Windows/macOS/Linux), Android app, iOS app, and self-hosted server. ZIM files are downloaded at home and stored on device or USB drive. This is the standard tool for pre-loading offline knowledge for expeditions, disaster response staging, and infrastructure-degraded environments. ZIM library: https://library.kiwix.org

U.S. Army Field Manuals (public domain): Numerous field manuals are publicly available via the Internet Archive (https://archive.org) and other sources:
- FM 21-76 Survival Manual: https://archive.org/details/Fm21-76SurvivalManual
- FM 21-76-1 Survival, Evasion, and Recovery: https://irp.fas.org/doddir/army/fm21-76-1.pdf
- FM 3-05.70 (updated survival manual) and many others are freely searchable at archive.org

FEMA Ready.gov (https://www.ready.gov/publications): Free downloads of hazard information sheets, emergency preparedness guides, and the full "Are You Ready?" citizen preparedness guide. Available in multiple languages. FEMA publications are government works in the public domain.

Survivor Library (https://www.survivorlibrary.com): Community-organized archive of pre-industrial and practical skills books, many public domain.

The awesome-survival GitHub list (https://github.com/alx-xlx/awesome-survival) is a community-curated index of survival/preparedness apps, datasets (including 22,000+ military manuals), and tools.

## First Aid and Medical Reference: TCCC, Stop the Bleed, and Field Apps

Tactical Combat Casualty Care (TCCC) is the evidence-based prehospital trauma care protocol developed by the U.S. Defense Health Agency Joint Trauma System. The TCCC guidelines (updated January 2024) are publicly available as PDFs:
- Current guidelines: https://learning-media.allogy.com/api/v1/pdf/f4cf1d4e-3191-443a-befc-415838fb04f2/contents
- TCCC Handbook v5 (Army): https://api.army.mil/e2/c/downloads/2023/01/19/31e03488/17-13-tactical-casualty-combat-care-handbook-v5-may-17-distro-a.pdf
- Quick Reference Guide (California EMSA): https://emsa.ca.gov/wp-content/uploads/sites/71/2017/07/TCCC_Quick_Reference_Guide_2017.pdf

NAEMT (https://www.naemt.org/education/trauma-education/naemt-tccc) is the primary civilian organization offering accredited TCCC courses for non-military personnel.

Stop the Bleed (https://www.stopthebleed.org): ACS (American College of Surgeons) public education campaign teaching hemorrhage control — tourniquet application, wound packing, and direct pressure. Free course materials and instructor kits available online.

For open-source mobile reference, the Survival Manual app (available on F-Droid: https://f-droid.org/en/packages/org.ligi.survivalmanual/) is a free, open-source, fully offline reference covering first aid, fire, water, navigation, and shelter topics. For structured wilderness medicine, GOES (https://www.goes.health) offers 67 offline protocols authored by wilderness medicine experts (not open-source but free tier available).

Red Cross First Aid app (https://www.redcross.org/take-a-class/first-aid/first-aid-apps) provides offline-capable step-by-step guidance for common emergencies and is freely available from the American Red Cross.

## Awesome Lists, Self-Hosted Tools, and Aggregators

Several curated GitHub 'awesome' lists aggregate preparedness and field tools:

- awesome-survival (https://github.com/alx-xlx/awesome-survival): Covers information archives (Wikipedia/Kiwix, military manuals, textbooks), communication (Ham radio, Meshtastic, ATAK, LoRaWAN), energy, and Android apps including the open-source Survival Manual.

- awesome-selfhosted (https://github.com/awesome-selfhosted/awesome-selfhosted): Curated list of services/software that can be self-hosted. Relevant for setting up local servers (Kiwix, map tile servers, OpenTAKServer, Nextcloud for file sync) on a LAN during extended field operations or disaster response.

- Linux-SDR (https://github.com/Slayingripper/Linux-SDR): Comprehensive list of SDR tools for Linux across applications from ADS-B aircraft tracking to weather satellite imagery.

For self-hosting map tiles locally (e.g., on a Raspberry Pi for a team LAN):
- TileServer GL (https://github.com/maptiler/tileserver-gl): Serves MBTiles offline map packages over HTTP for browser or app consumption.
- OpenMapTiles (https://openmaptiles.org): Pre-built planet extracts in MBTiles format based on OSM data, can be downloaded and served entirely offline.

For offline navigation on desktop/web:
- Marble (https://marble.kde.org): KDE offline map and virtual globe, works without internet, supports OSM and various other map layers.

### Checklist: Offline Field Device Preparation Checklist (before departing connectivity)

- [ ] Download OsmAnd or Organic Maps regional map packs for all areas of operation
- [ ] Import waypoints, routes, and base camp locations as GPX files
- [ ] Configure CHIRP with local repeaters, NOAA weather freqs, GMRS/FRS calling, and simplex emergency channels; write to radio
- [ ] Download Kiwix ZIM files: full Wikipedia, WikiHow first-aid articles, relevant field manual PDFs
- [ ] Load ATAK-CIV or CivTAK; configure team CoT server address or enable peer-to-peer mesh
- [ ] Configure Meshtastic nodes with shared channel key, device names, and team contact list
- [ ] Download FEMA hazard information sheets and TCCC Quick Reference Guide as PDF to device
- [ ] Export QGIS project with offline raster tiles to QField for any survey or assessment work
- [ ] Verify GPSBabel can read/write your device format; pre-load any required waypoints
- [ ] Test all apps in airplane mode before departure

### Checklist: TCCC / Stop the Bleed Response Priorities (MARCH mnemonic — reference only, get trained formally)

- [ ] M — Massive hemorrhage: apply tourniquet or wound packing to life-threatening bleeding first
- [ ] A — Airway: ensure airway is open; use recovery position or nasopharyngeal airway if trained
- [ ] R — Respiration: seal penetrating chest wounds; check for tension pneumothorax if trained
- [ ] C — Circulation: treat shock, establish IV/IO access if trained
- [ ] H — Hypothermia/Head injury: prevent heat loss; document neuro status
- [ ] Evacuate to higher care as rapidly as possible
- [ ] Full formal TCCC training available through NAEMT (naemt.org) and military/first-responder courses

### Checklist: Open-Source Radio / Comms Stack — Suggested Field Kit

- [ ] Baofeng UV-5R or UV-82 (or equivalent dual-band HT) programmed via CHIRP
- [ ] CHIRP-compatible USB cable stored with radio
- [ ] RTL-SDR v3 dongle + laptop with GQRX for spectrum monitoring and signal reception
- [ ] Meshtastic LoRa node (e.g., Heltec LoRa 32 v3 or LilyGO T-Beam) for encrypted text mesh
- [ ] Meshtastic Android or iOS app paired to node via Bluetooth
- [ ] Printed frequency reference card: local repeaters, NOAA weather, aviation guard (121.5 MHz), marine ch 16
- [ ] Backup battery / solar charger sized for multi-day operation

### Checklist: Kiwix Offline Content Priority Download List (high value per GB)

- [ ] Wikipedia (English, no-pic version ~20 GB; full with pics ~90 GB)
- [ ] WikiHow (all-languages, ~5 GB — procedures for first aid, tools, skills)
- [ ] Stack Overflow (developer/technical reference, ~50 GB)
- [ ] Project Gutenberg (classic texts, ~60 GB)
- [ ] Khan Academy (video-free version for offline education)
- [ ] Offline versions of relevant field manuals (load as PDF via any viewer, not ZIM)

## Resources & links

- [QGIS — Open Source GIS Desktop](https://qgis.org) — Primary open-source desktop GIS. Windows/macOS/Linux. GNU GPL.
- [QField — Mobile QGIS Field Collection App](https://qfield.org) — Open-source Android/iOS/desktop QGIS companion for offline field data collection. GitHub: github.com/opengisch/QField
- [OsmAnd — Offline Maps and Navigation](https://osmand.net) — Full-featured offline navigation app for Android and iOS using OSM data. F-Droid tracker-free build available.
- [Organic Maps — Offline Hike, Bike, and Navigation](https://organicmaps.app) — Lightweight, ad-free, open-source navigation app. Best for hiking/cycling/travel. Unlimited offline downloads.
- [OpenStreetMap](https://www.openstreetmap.org) — Community-maintained open map database underlying OsmAnd, Organic Maps, QField, and more. ODbL licensed.
- [CivTAK / ATAK — Civilian Team Awareness Kit](https://www.civtak.org) — Android situational awareness app with offline mapping, team tracking, and CoT messaging. Source: github.com/deptofdefense/AndroidTacticalAssaultKit-CIV
- [OpenTAKServer — Open Source TAK Server](https://docs.opentakserver.io) — Community TAK server for ATAK/WinTAK/iTAK clients. Runs on Raspberry Pi. GitHub: github.com/brian7704/OpenTAKServer
- [CHIRP — Ham Radio Programming Software](https://chirp.danplanet.com) — Free, open-source cross-platform (Win/Mac/Linux) memory channel programmer for hundreds of radio models. GNU GPL.
- [Gqrx SDR — Open Source Software Defined Radio Receiver](https://www.gqrx.dk) — Open-source SDR receiver GUI powered by GNU Radio. Supports RTL-SDR, HackRF, Airspy. GitHub: github.com/gqrx-sdr/gqrx
- [Meshtastic — Open Source Off-Grid LoRa Mesh Communication](https://meshtastic.org) — Open-source firmware for $20-60 LoRa hardware enabling encrypted, license-free mesh text comms with no infrastructure. GitHub: github.com/meshtastic/firmware
- [GPSBabel — GPS Data Conversion and Transfer](https://www.gpsbabel.org) — Converts and transfers GPS data among ~100 formats; transfers to/from Garmin and Magellan hardware. GNU GPL.
- [Kiwix — Offline Knowledge Browser](https://kiwix.org) — Offline browser for Wikipedia, WikiHow, Gutenberg, and many more via compressed ZIM files. ZIM library at library.kiwix.org
- [FM 21-76 U.S. Army Survival Manual (Internet Archive)](https://archive.org/details/Fm21-76SurvivalManual) — Public domain U.S. Army survival manual. Free download. Internet Archive also hosts 22,000+ other military field manuals.
- [TCCC Guidelines (January 2024) — Defense Health Agency](https://learning-media.allogy.com/api/v1/pdf/f4cf1d4e-3191-443a-befc-415838fb04f2/contents) — Current TCCC guidelines PDF from the Committee on Tactical Combat Casualty Care (CoTCCC). Public access.
- [FEMA Ready.gov — Free Publications](https://www.ready.gov/publications) — Free downloadable hazard information sheets, emergency preparedness guides, and the full 'Are You Ready?' citizen guide.
- [awesome-survival — Curated Preparedness Resource List](https://github.com/alx-xlx/awesome-survival) — Community-maintained GitHub list covering apps, archives, comms tools, energy, and community resources for preparedness.
- [RTL-SDR Blog — SDR Community Hub](https://www.rtl-sdr.com) — Primary community site for RTL-SDR hardware and open-source scanner software tutorials.
- [NAEMT — TCCC Courses for Civilians](https://www.naemt.org/education/trauma-education/naemt-tccc) — Accredited TCCC-CMC and TCCC-CLS courses endorsed by the Joint Trauma System and American College of Surgeons.
- [Stop the Bleed — Hemorrhage Control Training](https://www.stopthebleed.org) — ACS public education initiative for civilian tourniquet and wound-packing skills. Free course materials available online.
- [GNU Radio — Open Source SDR Framework](https://www.gnuradio.org) — Foundational open-source signal processing toolkit underlying GQRX and many other SDR applications.
