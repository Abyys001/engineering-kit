# Education features

Generated from `feature-map.json` (schema: `domains/_schema/SCHEMA.md`). 28 features.

## Core

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `education.course_catalog` Course catalog | Define courses/subjects offered, with descriptions, credits, and prerequisites. | high | none | none |
| `education.academic_calendar` Academic terms and calendar | Define academic years/terms/semesters that courses and enrollment are scoped to. | medium | none | none |
| `education.class_sections` Classes / sections | A scheduled offering (cohort) of a course, with an assigned instructor and roster capacity. | high | none | none |
| `education.enrollment` Enrollment | Register a student into a course/section, tracking status through the term. | high | none | none |
| `education.lesson_content` Lesson / course content | Author and deliver lesson content: pages, files, video, links, structured modules. | high | none | low |
| `education.assignments` Assignments | Create graded or ungraded tasks with due dates, instructions, and rubrics. | high | none | low |
| `education.submissions` Submissions | Students submit files/text/links against an assignment, with late tracking. | high | none | medium |
| `education.grading_gradebook` Grading and gradebook | Score submissions/exams and aggregate into a per-course, per-term gradebook. | high | none | low |
| `education.attendance` Attendance | Record student presence/absence per class session or day. | medium | none | low |
| `education.exams_quizzes` Exams and quizzes | Timed or untimed assessments with question banks, auto-grading, and attempts. | high | low | medium |

## Common

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `education.timetable` Timetable / class schedule | Weekly schedule of class sections, rooms, and instructors. | medium | low | none |
| `education.certificates` Certificates | Issue a completion/achievement certificate once course or program requirements are met. | medium | none | none |
| `education.report_cards` Report cards / transcripts | Aggregate grades across a term/program into a formatted report or transcript. | medium | none | low |
| `education.parent_guardian_access` Parent/guardian access | Let a guardian view a student's grades, attendance, and fees, and receive notices. | medium | none | none |
| `education.fees_billing` Fees and billing | Define fee structures/plans and collect tuition or program fees from students/guardians. | medium | none | none |
| `education.announcements` Announcements | Broadcast messages from staff to a course, section, or the whole institution. | high | low | low |
| `education.live_classes` Live / virtual classes | Video-conferenced class sessions linked to a section's timetable. | medium | high | none |
| `education.student_portal` Student portal | Student-facing hub for courses, grades, assignments, timetable, and messages. | high | low | none |

## Recommended

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `education.self_paced_content` Self-paced / packaged content | Deliver SCORM/H5P-style interactive packages that track completion and score. | medium | none | low |
| `education.rubrics` Rubrics | Structured scoring criteria attached to assignments/exams for consistent grading. | medium | none | none |
| `education.discussion_forums` Discussion forums | Threaded course discussion between students and instructors. | high | medium | low |
| `education.admissions` Admissions / applications | Manage prospective-student applications before they become enrollments. | medium | none | low |

## Optional

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `education.xapi_learning_records` Learning record tracking (xAPI) | Emit fine-grained learning activity statements to a Learning Record Store for cross-system analytics. | medium | none | medium |
| `education.plagiarism_detection` Plagiarism / AI-writing detection | Scan submissions against reference corpora and flag similarity or AI-generated content. | low | none | high |

## Premium

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `education.at_risk_student_prediction` At-risk student prediction | Flag students likely to fail or drop out from attendance, grade, and engagement signals. | low | none | high |

## Compliance

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `education.child_data_consent_controls` Child data / consent controls | Age-gate signup and require verifiable parental consent before collecting a minor's data. | low | none | none |

## Integration

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `education.lti_tool_integration` LTI tool integration | Launch external learning tools (publisher content, proctoring, plagiarism checkers) from inside a course with passed-through identity/context. | high | none | none |
| `education.roster_sync` Roster and gradebook sync | Interchange enrollment, class, and grade data with a school's Student Information System. | medium | none | none |
