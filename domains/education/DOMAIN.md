# Education (LMS / school management)

Learning management and school/institution administration: course delivery, enrollment, content, assessment, grading, attendance, and fees. No repository was cloned for this domain — researched via GitHub API inspection of doctype/model listings only (see `sources.md`).

## Product types
K-12 school management systems, higher-ed LMS, corporate/professional training platforms, and MOOC-style course platforms. Feature emphasis differs (attendance/fees/guardians matter most for K-12; LTI/roster-sync/accreditation matter most for higher-ed and enterprise LMS).

## Users
Student, guardian, instructor/teacher, teaching assistant, academic administrator/registrar, school/platform administrator, billing staff, exam proctor, system/integration account. See `roles.json`.

## Core workflows
Enrollment lifecycle, assignment submission & grading, exam/quiz lifecycle, admissions, certificate issuance, fee payment, live class session. State machines are informed by the three reference implementations (medium confidence — no external standard fixes these enums the way FHIR does for healthcare).

## Capabilities
- **Core**: course catalog, academic terms/calendar, class sections, enrollment, lesson/content delivery, assignments, submissions, grading/gradebook, attendance, exams/quizzes.
- **Common**: timetable, certificates, report cards/transcripts, parent/guardian access, fees & billing, announcements, live/virtual classes, student portal.
- **Recommended/optional**: rubrics, discussion forums, self-paced (SCORM/H5P) content, admissions, xAPI learning-record tracking, plagiarism/AI-writing detection.
- **Integration**: LTI tool launch, SIS roster/gradebook sync.
- **Compliance-classified**: child data/consent controls.
- **Premium**: at-risk student prediction (AI).

Full list with confidence/tags: `FEATURES.md`.

## Compliance-sensitive areas
FERPA (US student records), COPPA (US, under-13 data — K-12 products), GDPR incl. Art. 8 child consent (EU/EEA), web accessibility (WCAG 2.1/2.2, legally backed by Section 508/ADA in the US and EN 301 549 in the EU for public/higher-ed institutions), academic integrity policy (institutional guideline, not law — included because it directly shapes the plagiarism-detection feature). All `requires_human_review: true`; see `compliance.json` disclaimer.

## Integrations
Student Information System sync (OneRoster), LTI tool launch, video conferencing for live classes, payment gateways for fees, plagiarism/AI-writing checkers, SCORM/H5P content repositories, calendar sync, xAPI Learning Record Store.

## Entities
Student, Guardian, Instructor, Institution, AcademicTerm, Course, CourseSection, Enrollment, Lesson, Assignment, Submission, Grade, AttendanceRecord, TimetableSlot, Exam, ExamAttempt, Certificate, FeeInvoice, Announcement, DiscussionThread, Rubric. Roster/grade/course/enrollment/exam entities map to 1EdTech OneRoster/QTI concepts — see `entities.json` `standard_mapping`.

## UI patterns
Course/section grid, gradebook spreadsheet view, assignment submission drawer, timetable/calendar view, exam-taking interface with timer, threaded discussion view, certificate template renderer.

## Mobile
Student and guardian portals (grades, attendance, assignments, announcements, fee status) are the primary mobile surfaces; instructor grading has secondary mobile relevance.

## AI
Plagiarism/AI-writing detection, at-risk student prediction, engagement analytics from xAPI statements, application-screening assistance — all `ai_relevance: medium` or higher, none `core`.

## Standards
1EdTech LTI (tool launch), OneRoster (roster/grade interchange), QTI (assessment items/results), and ADL xAPI (learning activity statements) — all real, well-established industry standards, but this pass could not independently re-verify their publisher pages live (sandboxed network blocked outbound fetches to non-GitHub hosts), so they're cited at `medium` confidence with that caveat noted in `sources.md` rather than `high`.

## Terminology
LMS (learning management system), SIS (student information system), LTI (Learning Tools Interoperability), SCORM/xAPI (content packaging/activity-tracking formats), gradebook, rubric, cohort/section.

## Sources
Frappe Education (GPL-3.0, reference-only), Moodle (GPL-3.0, reference-only), Canvas LMS (AGPL-3.0, reference-only), plus the four standards above. Details: `sources.md`.
