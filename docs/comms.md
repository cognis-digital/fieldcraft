# Field communications

> **Disclaimer:** Educational / reference / preparedness material with links to public and open-source resources. Not operational instructions for violence or weapons. Verify against primary sources; train with qualified instructors. Follow all applicable laws.

Field communications encompasses the planning, equipment, protocols, and skills needed to maintain reliable radio contact across a range of scenarios — from day hikes and neighborhood preparedness groups to disaster response and tactical operations. The core principle is redundancy: a single radio on a single channel is a single point of failure. Every serious communicator — civilian or military — should have a PACE plan (Primary, Alternate, Contingency, Emergency) that layers independent technologies so communication survives degraded or denied conditions. This reference covers the PACE framework, unlicensed and licensed radio services (FRS, GMRS, MURS, amateur/ham), antenna and propagation fundamentals, operating etiquette and procedure words (prowords), the NATO phonetic alphabet, and open-source tools such as CHIRP for radio programming.

## The PACE Plan

PACE stands for Primary, Alternate, Contingency, Emergency. It is a communication planning methodology that originated in U.S. military doctrine and has been adopted by CISA, FEMA, and civilian preparedness communities. The goal is to define four independent, non-overlapping communication paths between any two parties so that if one fails, the next takes over without confusion.

The four tiers:
- PRIMARY: The everyday method, typically the most capable. Example: smartphone over cellular, or VHF/UHF repeater on a programmed GMRS or ham frequency.
- ALTERNATE: The first fallback when primary is unavailable. Example: FRS simplex walkie-talkies, a GMRS repeater on a different channel, or a mobile hotspot substituting for home internet.
- CONTINGENCY: Works but is slower, harder, or shorter-range. Example: HF radio (requires more skill but bypasses local infrastructure), satellite messenger (Garmin inReach / SPOT), or mesh network radio (Meshtastic LoRa).
- EMERGENCY: Last resort, high latency, expensive, or very low bandwidth. Example: HF CW Morse, written note via runner, signal mirror, or a pre-arranged visual signal.

Key design rules:
1. Each tier must be INDEPENDENT of the others — different frequency bands, different infrastructure, different power sources.
2. Define triggers — what condition causes a switch from P to A? Establish a time or condition threshold in advance ('if no contact on primary channel within 10 minutes, shift to alternate').
3. All parties must know the plan BEFORE an emergency. Publish the plan and rehearse it.
4. Power sources matter — a radio that depends on mains power or cell-charged batteries fails in a grid-down event. Solar, hand-crank, or alkaline backup is part of the plan.

CISA has published a guide specifically on integrating the PACE methodology into emergency communications ecosystems, available at https://www.cisa.gov/sites/default/files/2024-10/2024_NCSWICPTE_Leveraging_PACE_Plan_Emergency_Comms_Ecosystems.pdf

The FEMA ICS-205 Incident Radio Communications Plan form formalizes this concept for incident-command operations and is freely downloadable at https://training.fema.gov/emiweb/is/icsresource/assets/ics%20forms/ics%20form%20205,%20incident%20radio%20communications%20plan%20(v3.1).pdf

## Unlicensed Radio Services: FRS and MURS

These services require no FCC license and are accessible to anyone in the United States.

FAMILY RADIO SERVICE (FRS):
- 22 channels shared with GMRS in the 462–467 MHz UHF band
- Power limit: 2 watts on channels 1–14 (462 MHz); 0.5 watts on channels 15–22 (467 MHz)
- Radios must be FCC-certified and cannot be modified
- No license required; anyone can use them
- Typical range: 0.5–2 miles in real terrain (marketing figures of '35 miles' assume flat, open ground)
- Ubiquitous — sold at every big-box store; Motorola T800, Midland GXT, etc.
- CTCSS privacy codes (38 tones) and DCS codes (83 codes) let you squelch other conversations but do NOT encrypt and do NOT give you a private channel — others can still hear you if they disable tone squelch
- FCC page: https://www.fcc.gov/wireless/bureau-divisions/mobility-division/family-radio-service-frs

FRS CHANNELS (abbreviated):
  Ch 1: 462.5625 MHz | Ch 2: 462.5875 | Ch 3: 462.6125 | Ch 4: 462.6375 | Ch 5: 462.6625 | Ch 6: 462.6875 | Ch 7: 462.7125 (all 2W FRS / GMRS simplex)
  Ch 8: 467.5625 | Ch 9: 467.5875 | Ch 10: 467.6125 | Ch 11: 467.6375 | Ch 12: 467.6625 | Ch 13: 467.6875 | Ch 14: 467.7125 (all 0.5W FRS only)
  Ch 15–22: 462.5500–462.7250 MHz (2W FRS / GMRS simplex + GMRS repeater output)
  Note: Ch 9 (467.5875 MHz) is an informal emergency calling channel on many FRS radios.

MULTI-USE RADIO SERVICE (MURS):
- 5 channels in the VHF band (151–154 MHz); no license required
- Maximum power: 2 watts
- Channels: 151.820, 151.880, 151.940, 154.570 ('Blue Dot'), 154.600 ('Green Dot') MHz
- Bandwidths: 11.25 kHz on ch 1–3; 20 kHz on ch 4–5
- VHF penetrates foliage better than UHF but is more susceptible to terrain blockage at range
- No repeaters permitted on MURS; simplex only
- Good for farm/ranch use, trail communication, or anywhere you want VHF without a license
- FCC page: https://www.fcc.gov/wireless/bureau-divisions/mobility-division/multi-use-radio-service-murs

## Licensed Radio Services: GMRS and Amateur (Ham) Radio

GENERAL MOBILE RADIO SERVICE (GMRS):
- Requires an FCC license (no exam — just a $35 application through the FCC Universal Licensing System)
- License covers the applicant and their immediate family members; valid 10 years, renewable
- Eligibility: must be 18+ and not a representative of a foreign government
- 30 channels in the 462–467 MHz range, shared with FRS on many channels
- Power limits: 5 watts (handheld), 15 watts (mobile/base on certain channels), 50 watts (base station on specific channels)
- REPEATER access: GMRS licensees may use and build repeaters — this dramatically extends range. Repeater output is on 462.xxx MHz; input is 467.xxx MHz (+5 MHz offset).
- myGMRS.com (https://mygmrs.com) is the primary directory of GMRS repeaters in the US (1,700+)
- RepeaterBook (https://www.repeaterbook.com) also lists GMRS repeaters alongside ham repeaters
- FCC GMRS page: https://www.fcc.gov/wireless/bureau-divisions/mobility-division/general-mobile-radio-service-gmrs
- Apply for license via FCC ULS: https://www.fcc.gov/wireless/systems-utilities/universal-licensing-system

AMATEUR (HAM) RADIO:
The most capable and flexible of all personal radio services. Requires passing an FCC-authorized exam. Three license classes:

1. TECHNICIAN (entry level):
   - 35-question exam; no Morse code required
   - Privileges: all frequencies above 30 MHz (VHF/UHF), plus limited HF privileges (10m, parts of 40m/80m)
   - Covers 2m (144–148 MHz) and 70cm (420–450 MHz) — the most common VHF/UHF repeater bands
   - New question pool effective July 1, 2026

2. GENERAL:
   - 35-question exam; must hold Technician first
   - Privileges: adds most HF bands (global communication via skywave/NVIS)

3. AMATEUR EXTRA:
   - 50-question exam; most comprehensive
   - Privileges: all available US amateur bands and modes, including exclusive Extra-class sub-bands

License is issued free (after a $35 FCC administrative fee for new/upgraded licenses) and valid 10 years. Study resources:
- ARRL licensing portal: https://www.arrl.org/ham-radio-licenses
- HamStudy.org (free practice tests, 2026 Tech pool): https://hamstudy.org
- HamExam.org (free practice exams): https://www.hamexam.org
- FCC Amateur Radio Service page: https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service

VOLUNTEER EXAM SESSIONS: Found via https://hamstudy.org/sessions — exams are given by Volunteer Examiners (VEs) at community events, club meetings, and online sessions. Cost is typically $15–$35.

ARES (Amateur Radio Emergency Service): ARRL-organized volunteers who provide communications backup during disasters. Open to all licensed hams. Coordinate with local emergency management. Join via https://www.arrl.org/ares

## Antenna and Propagation Fundamentals

Understanding how radio waves travel is essential for effective field use. Different frequency bands behave very differently.

FREQUENCY BANDS RELEVANT TO FIELD COMMS:
- HF (High Frequency): 3–30 MHz. Waves can travel via ground wave (short range, up to ~300 miles) or ionospheric skywave (NVIS and long-range DX). The workhorse for long-distance field comms.
- VHF (Very High Frequency): 30–300 MHz. Mostly line-of-sight (LOS). Penetrates foliage better than UHF. MURS, FM broadcast, 2m ham band live here.
- UHF (Ultra High Frequency): 300 MHz–3 GHz. Strictly LOS. FRS/GMRS/70cm ham band here. Shorter wavelength means smaller antennas, better penetration of buildings in urban environments.

PROPAGATION MODES:
- Line of Sight (LOS): VHF/UHF; signals travel in a straight line. Terrain, buildings, and trees block them. Repeaters placed on hilltops extend coverage dramatically.
- Ground Wave: HF; signal hugs the Earth's surface, reliable to 300 miles on lower HF bands (160m, 80m, 40m).
- Skywave / Ionospheric: HF signals bounce off ionosphere layers. Enables transoceanic communication on 20m, 15m, 10m. Varies by time of day, season, and solar cycle.
- NVIS (Near Vertical Incidence Skywave): A specialized HF mode where the antenna radiates nearly straight up, signals bounce off the low ionosphere and rain down in a 100–300 mile radius. Ideal for regional disaster communications (county to state EOC). Uses 40m (7 MHz) by day, 80m (3.5–4 MHz) at night. The antenna is a horizontal half-wave dipole hung LOW (7–15 feet off the ground). The U.S. military's AS-2259 antenna is a classic NVIS design; homebrew versions are easy to build.

ANTENNA TYPES USEFUL IN THE FIELD:
- Half-wave dipole: Two equal wire legs fed at center. Easy to build from speaker wire or WD-14 field wire. Length formula: 468 / frequency(MHz) = total length in feet. Half that per leg. Can be strung between trees.
- End-fed half-wave (EFHW): Single wire fed at one end via a matching transformer (UNUN). Easier to deploy in field — only needs support at one end.
- Vertical (whip): Quarter-wave vertical with ground radials. Omnidirectional. The rubber duck antenna on a handheld is a compromised vertical — external whip or roll-up J-pole significantly improves performance.
- J-pole: A popular VHF/UHF antenna, easily built from 300-ohm twin-lead TV cable. Good gain, no ground plane needed.
- Yagi (beam): Directional antenna for longer-range point-to-point VHF/UHF. More complex to build but high gain.

PRACTICAL RULES:
1. Height = range for VHF/UHF. Get the antenna as high as safely possible.
2. For HF NVIS, low = better. A dipole at 10 feet is an NVIS antenna. A dipole at 50 feet is a DX antenna.
3. Coax loss matters. RG-58 is fine for VHF up to 50 feet. Use LMR-400 or better for longer runs or UHF.
4. A proper antenna beats a powerful radio every time. Double power gives +3 dB. A better antenna can give 6–10 dB.
5. CHIRP software (https://chirpmyradio.com) is the standard tool for programming channel memories, CTCSS/DCS tones, and offsets into Baofeng, Kenwood, Yaesu, and hundreds of other radios via a USB cable.

## Operating Procedures and Prowords

Standardized procedure words (prowords) reduce ambiguity and save airtime. They are used by military, aviation, maritime, and amateur emergency nets. The most critical ones to know:

CORE PROWORDS:
- OVER: 'My transmission is ended; I expect your response.' (Pronounced at the end of each transmission in a back-and-forth exchange.)
- OUT: 'Conversation is complete; no response required.' Never say 'OVER AND OUT' — they are mutually exclusive.
- ROGER: 'I have received your last transmission satisfactorily.' Does NOT mean 'I will comply.'
- WILCO: 'I have received, understand, and will comply.' Includes ROGER implicitly — never say 'ROGER WILCO.'
- SAY AGAIN: 'Repeat your last transmission.' (Do NOT say 'REPEAT' on a military net — REPEAT is an artillery fire command ordering another fire mission.)
- BREAK: 'I am separating two parts of a message.' Also used by a third station to interrupt an in-progress transmission for priority traffic.
- WAIT / WAIT OUT: 'Stand by; I will resume shortly.' WAIT OUT means the pause will be longer.
- NEGATIVE: 'No' or 'That is incorrect.'
- AFFIRMATIVE: 'Yes' or 'That is correct.' (Plain 'yes' is also acceptable in most contexts.)
- SEND YOUR TRAFFIC: 'Proceed with your message.'
- RADIO CHECK: 'What is my signal strength and readability?' Response uses the SINPO/RST scale or a plain description ('Lima Charlie' = Loud and Clear).
- NET CALL: Calling all stations on the net simultaneously.
- THIS IS: Precedes your own call sign to identify yourself.
- UNKNOWN STATION: Addressing an unidentified station.
- FIGURES: Indicates that numbers follow and should be read digit by digit.
- AUTHENTICATE: Challenges the other party to prove identity using a pre-arranged authentication table.

CALLING PROCEDURE (example):
'[Station called], [Station called] — THIS IS [your call sign] — OVER.'
Response: '[Your call sign] — THIS IS [station called] — SEND YOUR TRAFFIC — OVER.'

NET DISCIPLINE:
- Listen before transmitting (LBT). If the channel is in use, wait for a pause.
- Keep transmissions brief. Think before keying the mic.
- Identify yourself — FCC Part 97 requires amateur stations to ID at the end of transmissions and at least every 10 minutes during a contact.
- On a directed net, only the Net Control Station (NCS) opens the floor. Check in by giving your call sign; wait to be recognized.
- On GMRS/FRS, use plain English. CTCSS tones are set before the field operation and noted in the PACE plan.
- Brevity codes can be used but must be pre-agreed. In unplanned emergencies, plain language is safer.

REPEATER DISCIPLINE:
- Program the correct CTCSS/DCS access tone and the +/- offset before going to the field.
- Use minimum power to access the repeater reliably.
- Courtesy tones: wait for the repeater to drop its squelch tail before transmitting again.
- Move lengthy non-emergency conversations to a simplex frequency.

Resources:
- Wikipedia Procedure Word article: https://en.wikipedia.org/wiki/Procedure_word
- USCG Auxiliary radio communications guide: https://wow.uscgaux.info/content.php?unit=070-09-03&category=radio-communication

## NATO Phonetic Alphabet

The NATO/ICAO phonetic alphabet assigns a unique spoken code word to each letter of the Latin alphabet. Adopted March 1, 1956 and used by NATO, ICAO, ITU, and amateur radio operators worldwide. Each word was specifically chosen to be acoustically distinct from all others, even when distorted by noise or spoken by a non-native English speaker.

FULL ALPHABET:
  A — Alfa      (not 'Alpha' — avoids confusion across languages)
  B — Bravo
  C — Charlie
  D — Delta
  E — Echo
  F — Foxtrot
  G — Golf
  H — Hotel
  I — India
  J — Juliett   (two t's)
  K — Kilo
  L — Lima      (LEE-mah)
  M — Mike
  N — November
  O — Oscar
  P — Papa
  Q — Quebec    (keh-BEK)
  R — Romeo
  S — Sierra
  T — Tango
  U — Uniform
  V — Victor
  W — Whiskey
  X — X-ray
  Y — Yankee
  Z — Zulu

NUMBERS: Spoken digit by digit. Special pronunciation: 3 = 'Tree', 4 = 'Fow-er', 5 = 'Fife', 9 = 'Niner' (to distinguish from German 'nein' = no).

USAGE EXAMPLE: Call sign KD9XYZ = 'Kilo Delta Niner X-ray Yankee Zulu.'
Coordinate grid: '4 7 Tree 5' (473.5).

Official NATO page: https://www.nato.int/en/news-and-events/articles/news/2017/12/21/nato-phonetic-alphabet-codes-and-signals

## CHIRP and Open-Source Radio Tools

Programming radios manually via front-panel menus is error-prone and slow, especially when configuring repeater offsets, CTCSS tones, and dozens of channel memories before a field deployment. CHIRP is the standard free, open-source solution.

CHIRP:
- Website/download: https://chirpmyradio.com/projects/chirp/wiki/Download
- Runs on Windows, macOS, Linux
- Supports hundreds of radios from Baofeng, Yaesu, Kenwood, Icom, Motorola, Anytone, TYT, and others
- Spreadsheet-like GUI: edit channels, frequencies, tones, offsets, names, and upload to radio via USB programming cable
- Import/export from/to CSV, RepeaterBook, myGMRS, and other sources
- Two active releases: CHIRP-Next (recommended) and CHIRP Legacy (maintenance only)
- Community forums and wiki at chirpmyradio.com
- Entirely volunteer-developed, free of charge, open-source (Apache License)

OTHER USEFUL OPEN-SOURCE AND FREE TOOLS:
- RepeaterBook (https://www.repeaterbook.com): Free, crowd-sourced database of US and international ham and GMRS repeaters. Can export directly to CHIRP.
- myGMRS (https://mygmrs.com): GMRS-specific repeater directory. Requires registration with call sign. Map view for field planning.
- HamStudy.org (https://hamstudy.org): Free exam prep, flash cards, full question pools for all three license classes.
- HamExam.org (https://www.hamexam.org): Free practice exam generator.
- APRS.fi (https://aprs.fi): Real-time map of APRS (Automatic Packet Reporting System) — shows ham radio stations, weather, and Winlink gateway locations on a web map.
- Winlink (https://www.winlink.org): Free, open system for sending email over HF/VHF amateur radio when internet is down. Used extensively in ARES/RACES operations.
- JS8Call (https://js8call.com): Keyboard-to-keyboard weak-signal HF messaging mode derived from FT8. Designed for EmComm.
- Meshtastic (https://meshtastic.org): Open-source LoRa mesh radio firmware for off-grid text messaging. Runs on inexpensive ($30–60) LoRa devices. No license required at low power on ISM frequencies.
- SDR# / SDRangel (https://airspy.com/download/): Free software-defined radio tools for use with $25 RTL-SDR dongles — allows monitoring of FRS/GMRS/VHF/UHF traffic for situational awareness.

## Field Communications Checklist and PACE Planning Worksheet

Use the following checklists when planning communications for a field deployment, preparedness group, or emergency net.

BEFORE DEPARTING (GO-KIT CHECKLIST):
- Primary radio programmed, battery charged, spare battery or solar charger packed
- Alternate radio (different technology/band) charged and programmed
- Antenna for each radio — external whip or roll-up J-pole stored in kit
- USB programming cable + CHIRP-loaded laptop or backup channel card (laminated)
- PACE plan printed and distributed to all team members
- Repeater tones (CTCSS/DCS) and offsets verified in radio memories
- Authentication codes / challenge-response card if used
- Power bank / solar panel / alkaline battery tray as backup power
- Ear/mic headset for noisy environments
- Scan list programmed to monitor multiple channels simultaneously

PACE PLAN TEMPLATE (fill in for your group):
  P — Primary channel: ___ MHz, tone ___, mode ___
  A — Alternate channel: ___ MHz, tone ___, mode ___
  C — Contingency: ___ (e.g., HF 40m simplex at 7.285 MHz / MURS ch 3)
  E — Emergency: ___ (e.g., FRS ch 9 / written note via runner / signal mirror)
  Trigger: switch from P to A if no contact in ___ min
  Authentication: challenge word ___ / response ___
  Schedule: check-ins at ___ and ___ local time

FIELD COMMUNICATIONS QUICK RULES:
1. PACE plan known by all parties before the event.
2. Listen before transmit — always.
3. Short, clear transmissions — think, then speak.
4. NATO phonetic alphabet for all letters, call signs, and grid coordinates.
5. SAY AGAIN (not REPEAT) for requesting a retransmission.
6. End transmissions with OVER (expecting reply) or OUT (conversation done).
7. ROGER means received; WILCO means received and will comply.
8. On licensed bands, ID by call sign as required by FCC rules.
9. Simplex first for direct comms; repeater for extended range.
10. Minimum power necessary for the link — do not QRM others unnecessarily.

### Checklist: Go-Kit / Field Radio Kit

- [ ] Primary radio: battery charged, programmed, external antenna attached or stored
- [ ] Alternate radio (different service/band): charged and programmed
- [ ] Contingency device (HF radio, sat messenger, or LoRa mesh node)
- [ ] USB programming cable + CHIRP installed on laptop or Chromebook
- [ ] Laminated backup channel/frequency card (does not need power)
- [ ] PACE plan printed — one copy per team member
- [ ] Repeater CTCSS/DCS tones verified against RepeaterBook or myGMRS
- [ ] Simplex backup frequencies programmed alongside repeater channels
- [ ] Spare batteries or alkaline battery tray for each radio
- [ ] Solar panel or power bank (minimum 10,000 mAh) for recharging
- [ ] Headset/earpiece with PTT for covert or high-noise environments
- [ ] Roll-up J-pole or telescoping whip antenna for VHF/UHF improvement
- [ ] For HF: lightweight dipole wire, center insulator, and 50-ohm coax
- [ ] Frequency reference card (FRS/GMRS channels, ham bands, MURS)

### Checklist: PACE Plan Verification Checklist

- [ ] All four tiers (P/A/C/E) defined and written down
- [ ] Each tier uses independent infrastructure (different bands, frequencies, or technologies)
- [ ] Trigger conditions defined: when to shift from P to A, A to C, C to E
- [ ] Schedule defined: check-in times, guard frequencies, and listening windows
- [ ] All team members have received and read the plan
- [ ] Plan rehearsed at least once before deployment or event
- [ ] Authentication challenge/response defined if security matters
- [ ] Battery/power contingency addressed for each tier
- [ ] Alternative to PACE (runner, visual signals) defined as absolute last resort

### Checklist: Getting Licensed (Ham Radio) Checklist

- [ ] Choose entry level: Technician for local VHF/UHF; plan for General if HF is needed
- [ ] Study at HamStudy.org (https://hamstudy.org) — free, covers current question pool
- [ ] Practice at HamExam.org (https://www.hamexam.org) with timed mock exams
- [ ] Score consistently 80%+ on practice exams before scheduling the real test
- [ ] Find an exam session at https://hamstudy.org/sessions — search by ZIP code
- [ ] Bring: government-issued ID, FCC FRN number (register free at https://www.fcc.gov/wireless/support/universal-licensing-system/getting-fcc-registration-number-frn), exam fee (~$15–35 cash)
- [ ] After passing: FCC posts license to ULS in 1–2 business days — do NOT transmit until callsign appears in FCC database
- [ ] Pay the $35 FCC application fee at https://www.fcc.gov within 10 days of exam
- [ ] Once licensed: join local ARES group via https://www.arrl.org/ares
- [ ] Program your radio using CHIRP and a local repeater from RepeaterBook

### Checklist: Radio Net Operating Quick Reference

- [ ] Listen before transmitting — confirm channel is clear
- [ ] Identify yourself by call sign at start and end of transmission (required by FCC for ham)
- [ ] Use NATO phonetic alphabet for all letters, call signs, and grid coordinates
- [ ] SAY AGAIN to request a repeat (not REPEAT on a military/tactical net)
- [ ] ROGER = received only; WILCO = received and will comply; never say ROGER WILCO
- [ ] OVER = expecting reply; OUT = conversation ended; never use both together
- [ ] Keep transmissions concise — think before keying the mic
- [ ] Use minimum power needed for reliable communication
- [ ] On a directed net, wait for Net Control Station to call you before transmitting
- [ ] BREAK to interrupt for urgent/emergency traffic
- [ ] For emergency call: MAYDAY MAYDAY MAYDAY (distress) or BREAK BREAK BREAK (urgent) on any monitored frequency

## Resources & links

- [FCC: General Mobile Radio Service (GMRS)](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/general-mobile-radio-service-gmrs) — Official FCC GMRS rules, license requirements, power limits, and channel allocations
- [FCC: Family Radio Service (FRS)](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/family-radio-service-frs) — Official FCC FRS rules; 22 channels, power limits, no-license requirements
- [FCC: Multi-Use Radio Service (MURS)](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/multi-use-radio-service-murs) — Official FCC MURS rules; 5 VHF channels, 2W max, license-free
- [FCC: Amateur Radio Service](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service) — FCC page for amateur radio licensing, regulations, and ULS access
- [ARRL: Ham Radio Licenses](https://www.arrl.org/ham-radio-licenses) — ARRL overview of Technician/General/Extra license classes, exam prep, and getting started
- [ARRL: Amateur Radio Emergency Service (ARES)](https://www.arrl.org/ares) — How to join and participate in ARES for disaster and emergency communications
- [HamStudy.org — Free Exam Prep (includes 2026 Tech pool)](https://hamstudy.org) — Flash cards, practice tests, full question pools for all three license classes; updated for 2026 Technician pool
- [HamExam.org — Free Practice Exams](https://www.hamexam.org) — Timed, full-length mock exams mirroring actual FCC exam format
- [CHIRP Radio Programming Software](https://chirpmyradio.com/projects/chirp/wiki/Download) — Free, open-source tool for programming hundreds of radio models (Baofeng, Yaesu, Kenwood, etc.); Windows/macOS/Linux
- [RepeaterBook — Repeater Directory](https://www.repeaterbook.com) — Crowd-sourced directory of ham and GMRS repeaters in US and worldwide; integrates with CHIRP
- [myGMRS.com — GMRS Repeater Network](https://mygmrs.com) — Primary GMRS repeater directory and community; map view; 1,700+ repeaters
- [CISA: Leveraging the PACE Plan (PDF)](https://www.cisa.gov/sites/default/files/2024-10/2024_NCSWICPTE_Leveraging_PACE_Plan_Emergency_Comms_Ecosystems.pdf) — 2024 CISA paper on applying PACE methodology to civilian and government emergency communications ecosystems
- [FEMA ICS-205 Incident Radio Communications Plan (PDF form)](https://training.fema.gov/emiweb/is/icsresource/assets/ics%20forms/ics%20form%20205,%20incident%20radio%20communications%20plan%20(v3.1).pdf) — Fillable FEMA form for documenting all radio frequencies and assignments during an incident; free to use
- [NATO Phonetic Alphabet — Official NATO Page](https://www.nato.int/en/news-and-events/articles/news/2017/12/21/nato-phonetic-alphabet-codes-and-signals) — Official NATO article on phonetic alphabet, Morse code equivalents, and signals
- [Wikipedia: Procedure Word (Prowords)](https://en.wikipedia.org/wiki/Procedure_word) — Comprehensive list of standard radiotelephony procedure words with meanings and usage context
- [Winlink — Email Over Radio](https://www.winlink.org) — Free system for sending email over HF/VHF/UHF amateur radio when internet is down; used by ARES/RACES
- [Meshtastic — Off-Grid LoRa Mesh Messaging](https://meshtastic.org) — License-free ISM-band mesh radio for text messaging; $30–60 devices; no infrastructure needed
- [FRS/GMRS Combined Channel Chart — RadioReference Wiki](https://wiki.radioreference.com/index.php/FRS/GMRS_combined_channel_chart) — Complete tabular listing of all 22 FRS and 30 GMRS frequencies, power limits, and channel designations
