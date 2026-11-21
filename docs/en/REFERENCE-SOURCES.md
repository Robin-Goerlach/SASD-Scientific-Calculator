# Historical research references and provenance

**Purpose:** citations and future conformance research only. These sources are **not** permission to republish text, ROMs, images, firmware or included program libraries. Verify every reference program's license before committing fixtures.

## Series 41 and synthetic programming

- William C. Wickes, *Synthetische Programmierung auf dem HP-41C/CV* (German translator Heinz Dalkowski): https://www.mh-aerotools.de/hp/heldermann/Synthetische%20Programmierung%20auf%20dem%20HP-41C-CV.pdf
- Karl-Heinz Gosmann, *Anwenderhandbuch HP-41C/CV*, Vieweg, 1983: https://literature.hpcalc.org/community/hp41-anwenderhandbuch.pdf
- Historical Time Module and Statistics Pac manuals: source/edition and rights require independent recording before implementation.
- Advantage Pac: consult appropriate documented functional indexes; independently author all SASD adapters and tests. Do **not** assume XROM binary compatibility.

## Series 48 / System RPL

- Jim Donnelly, *An Introduction to HP 48 System RPL and Assembly Language Programming*: https://literature.hpcalc.org/items/1474
- Eduardo Kalinowski, *Programming in System RPL*: https://literature.hpcalc.org/items/1695
- Related System RPL second edition: https://literature.hpcalc.org/items/1696
- Further official calculator-family documentation, ROM compatibility references and independent emulators must be reviewed with exact version, observation and license details.

## Reference emulator/tool study

Emulators and converters can be **independent observation sources**, subject to version and rights assessment. Candidate tools raised in project discussion:

- V41: https://hp.giesselink.com/v41.htm
- Emu41: https://jeffcalc.hp41.eu/emu41/index.html
- LIFUTILS documentation: https://www.hhcworld.com/files/hpmo/lifutils-doc/tutorial.html

**Do not** include proprietary ROM dumps or republish test programmes from third parties without rights. An emulator result alone does not prove historical accuracy; triangulate with published manuals and, where available, lawful device observations.

## Fixture provenance template

```text
fixture_id:
model_and_rom_profile:
historical_command_or_object:
source_title_and_version:
source_url:
copyright_and_redistribution_license:
independent_observation:
expected_state_and_error:
numeric_tolerance:
automated_test_path:
last_verified_date:
known_deviations:
```

If provenance is missing, label the example *research only*, not a redistributable golden fixture.
