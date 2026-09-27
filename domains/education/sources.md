# Education sources

Class, license, and what each source informed. Full records: `feature-map.json` → `sources`.

| ID | Title | Type | License | Local clone | Informed |
|---|---|---|---|---|---|
| `frappe-education` | [Frappe Education](https://github.com/frappe/education) | implementation | GPL-3.0 | — | `academic_calendar`, `admissions`, `assignments`, `attendance`, `certificates`, `child_data_consent_controls`, `class_sections`, `course_catalog`, `enrollment`, `exams_quizzes`, `fees_billing`, `grading_gradebook`, `parent_guardian_access`, `report_cards`, `submissions`, `timetable` |
| `moodle` | [Moodle](https://github.com/moodle/moodle) | implementation | GPL-3.0 | — | `announcements`, `assignments`, `course_catalog`, `discussion_forums`, `enrollment`, `exams_quizzes`, `grading_gradebook`, `lesson_content`, `live_classes`, `lti_tool_integration`, `self_paced_content`, `student_portal`, `submissions` |
| `canvas-lms` | [Canvas LMS](https://github.com/instructure/canvas-lms) | implementation | AGPL-3.0 | — | `announcements`, `assignments`, `class_sections`, `course_catalog`, `discussion_forums`, `enrollment`, `exams_quizzes`, `grading_gradebook`, `lesson_content`, `plagiarism_detection`, `rubrics`, `student_portal`, `submissions` |
| `1edtech-lti` | [1EdTech Learning Tools Interoperability (LTI)](https://www.1edtech.org/standards/lti) | authoritative | 1EdTech public specification; free to implement, certification/trademark use requires 1EdTech membership | — | `lti_tool_integration` |
| `1edtech-oneroster` | [1EdTech OneRoster](https://www.1edtech.org/standards/oneroster) | authoritative | 1EdTech public specification; free to implement, certification/trademark use requires 1EdTech membership | — | `roster_sync` |
| `1edtech-qti` | [1EdTech Question and Test Interoperability (QTI)](https://www.1edtech.org/standards/qti) | authoritative | 1EdTech public specification; free to implement, certification/trademark use requires 1EdTech membership | — | `exams_quizzes` |
| `adl-xapi` | [xAPI (Experience API)](https://adlnet.gov/projects/xapi/) | authoritative | Published by ADL Initiative (US DoD); specification is openly published, exact reuse terms not independently re-verified this pass | — | `at_risk_student_prediction`, `xapi_learning_records` |

## Notes per source

### frappe-education
- Retrieved: 2026-09-27; version: main branch, 2026-09-26 snapshot
- Not cloned; inspected via GitHub API doctype listing (license.txt confirms 'GNU GPL V3'). Reference-only. Very rich doctype set: academic_year/term, course/course_enrollment, class_room, fee_plan/fee_schedule/fees, grade_book/grading_scale, assessment_plan/assessment_result, student_attendance, student_guardian, admission_register, ceremony (certificate/graduation). No code copied.

### moodle
- Retrieved: 2026-09-27; version: main branch, 2026-09-26 snapshot
- Not cloned; inspected via GitHub API (`public/mod/` activity module list: assign, quiz, forum, lesson, workshop, feedback, choice, scorm, h5pactivity, lti, glossary, wiki, book, bigbluebuttonbn). Reference-only. Confirms LTI as a first-class integration and the assignment/quiz/forum activity taxonomy. No code copied.

### canvas-lms
- Retrieved: 2026-09-27; version: main branch, 2026-09-26 snapshot
- Not cloned; inspected via GitHub API (repo license field AGPL-3.0; `app/models/` listing). Reference-only. Confirms assignment/assignment_group/assignment_override, appointment_group + calendar_event (scheduling), context_module (course content organization), conversation (messaging), announcement models. No code copied.

### 1edtech-lti
- Retrieved: 2026-09-27; version: LTI 1.3 / Advantage
- Standard for launching external learning tools from an LMS with authenticated context. Well-established industry standard (also confirmed present as Moodle's `mod/lti`); this pass could not independently re-verify the publisher page live (sandboxed network blocked the fetch), so confidence is kept medium rather than high pending a live re-check.

### 1edtech-oneroster
- Retrieved: 2026-09-27; version: OneRoster 1.2
- Standard for interchange of roster/enrollment/gradebook data between a school SIS and an LMS. Same live-verification caveat as 1edtech-lti.

### 1edtech-qti
- Retrieved: 2026-09-27; version: QTI 3.0
- Standard for representing assessment/quiz items and results portably. Same live-verification caveat as 1edtech-lti.

### adl-xapi
- Retrieved: 2026-09-27; version: xAPI 2.0
- Standard for recording learning experience statements ('actor verb object') across systems, successor to SCORM's tracking model. Live re-verification of the publisher page failed in this sandbox (network/TLS restrictions); treated as well-established from training knowledge, confidence kept medium.
