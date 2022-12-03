# CSE138 Fall 2020
## Distributed Systems
| key | value | 
|-----|-------|
|When: | Monday, Wednesday and Friday at <b>8:00 AM (yikes!)</b>. |
|Where: | Peter Alvaro's zoom room |
|Who: | [Peter Alvaro](http://people.ucsc.edu/~palvaro/) |
|Office hours: | TBD|
|Prerequisites: | (CSE101 or CE150) and CSE130 required. |
|Optional Text: | [Distributed Systems](http://www.amazon.com/Distributed-Systems-Concepts-Design-5th/dp/0132143011/), Coulouris et al.|
|TA: | Aleck Zhang and TBD|
|TA sections: | TBD|
|Modules: | [Modules](modules.md)|
|Readings (in flux): | [Readings](readings.md)|
|Midterm Date:| in class on Friday 11/6|

# Description

This course will explore fundamental as well as emerging topics in distributed systems.

Distributed systems are notoriously difficult to program, and even harder to reason about.  Much of this difficulty arises from *uncertainty* in the executions of distributed programs.  Uncertainty about the ordering and timing of events and communication give rise to concerns about the *consistency* of program outputs and states. Uncertainty about what may go wrong during an execution (e.g., computers crashing, messages being lost) gives rise to concerns about the *completeness* of these outputs and states.  Together, these sources of uncertainty make achieving even relatively modest guarantees in large-scale systems extremely difficult.

While distributed systems have been studied for some time, they have only recently become essentially ubiquitous:
nearly all non-trivial systems are now physically distributed.  It is no longer possible to relegate responsibility for managing the complexity of distributed systems to a group of expert library or infrastructure writers: all programmers must now be distributed programmers. This is both a crisis and an opportunity.

This course will cover both theoretical and practical aspects of distributed systems and distributed programming, diving the subject
matter into four core [Modules](modules.md):

 * Time and Asynchrony
 * Fault Tolerance
 * Consistency
 * Parallelism and Scaleup

 
# Readings and Prerequisites

The optional text for CMPS138 is [Distributed Systems](http://www.amazon.com/Distributed-Systems-Concepts-Design-5th/dp/0132143011/) by Coulouris et al.  Despite having perhaps the worst cover art that I have ever seen on any book in my life, this text covers most of the fundamental
concepts of the course.  Note however that the text is supplemental.  The key material of this course is covered in lecture, and reading the text will not be sufficient to pass the examinations.

For optional reading, Mikito Takada's [Distributed Systems for fun and profit](http://book.mixu.net/distsys/) covers 
many of the same topics in a sophisticated (albeit high-level) way.

Students are required to have completed either CMPS101 or CE150, and are recommended to have completed CMPS111 or CMPS105.

One of the purposes of CMPS138 is to familiarize you with practical aspects of implementing and reasoning about programs that 
require the cooperation of some number of physical machines.  Hence system building is a critical part of the course.
While CMPS138 will involve a substantial implementation component, we will not be teaching any particular language.
That is to say, you are here to build *distributed* systems, 
but we expect you to come to the table with enough programming knowledge and experience to build non-distributed systems with minimal guidance.  Regardless of the coursework you have undertaken, if you are not comfortable using programming languages 
(e.g. C, Java, Python, Ruby, Scala, Erlang, Bloom -- pick your poison) to build systems, this course is not for you.



 
# Assigments and Grading

## Final Project

The final project will involve implementing and managing fault-tolerant distributed system.  This will be a substantial enginering effort, and we encourage you to work in teams of up to four people.

The final project will be divided into four sub-projects, coming due roughly every two weeks.

Project specifications will be posted on a separate page and announced on Piazza.  They will usually be posted before they are announced, but they are subject to change until announcement.  If we need to change an assigment after it was announced, we will email the class about the change.

Assigments announcements will always include a due date.  

<del>Late assignments are not accepted</del>.  Late assignments will forfeit 10% of the grade for every day late.  Students are granted *one grace day* that they may use for any assignment submission to avoid this penalty.


## Examinations

There will be two examinations: the midterm and the final.

## Grading

| Subject | Share |
|-------|---------|
| Participation | 10% |
| Midterm | 20% |
| Project | 40% |
| Final   | 30%   | 

Final projects are required to pass the course.  The fact that participation accounts for 10% of the grade (and pop quizzes for 5%) should give you an idea of the important of class attendance.  

# Logistics

## Getting in

Undergraduate Computer Science courses at UCSC are severely impacted by high enrollments. Unfortunately this makes it difficult to register for courses, particularly if you are registering late, major in a different subject, or are a graduate student.

Although it is rarely possible to increase enrollment for the course due to external constraints (e.g., the size of the room and the availability of TAs), the course typically sees some attrition during the first few weeks.  I cannot promise a slot, but if you are in need of a permission code my recommendation is that you attend class for the first few weeks to see if a spot opens up.

## Getting Help

The material in this class can be complex and difficult, so there are several ways to get help with concepts covered in class, homework, and programming projects, listed in approximately the order you should try them for help.

 * Attend classes and lab sections.
 * Read (really read!) the assignments and other course materials.
 * Read and post to the class discussion forum on Piazza
 * Meet with the course staff during office hours.
 * Send a private piazza post to the course staff.
 
You’re encouraged to post general questions to the Piazza forum, and to answer questions others have posted there. Asking things like "how does this concept work?" or "can someone help install Ubuntu LINUX 18.04 on VirtualBox?" are fine. Questions such as "can someone post sample code for Assignment 2" or "why doesn’t the attached code work?" are not acceptable, and should be asked during office hours (preferable), or via private Piazza messages. Course staff will also read the forum and reply to posted questions.

Office hours are your chance to ask the course staff in-depth questions about the material being covered, programming assignments (including debugging help), or anything else about computer system design or other general computer science issues you want to discuss. Many students find that discussions in office hours are highly informative and interesting, and it usually helps faculty members write you better recommendations for jobs and graduate school. If you can’t attend office hours, arrange a meeting in advance by using a private Piazza message

Private Piazza questions will typically get a response by the end of the next business day.  Public ones will probably get answered sooner, since they have hundreds of eyes on them!  Please do not email the course staff directly unless asked -- this way we can keep all communication related to the class in one place and avoid overlooking your messages.


# Academic honesty

Collaboration is a key part of research.  I encourage you to discuss the readings and the final project ideas with your classmates.  However, you must reveal the students with whom you discussed the assignments.  Failure to do so will result in formal disciplinary proceedings.  

I should not need to say so, but I do: plagiarism in any form is not acceptable and will not be tolerated.  As researchers, we always stand upon the shoulders of giants, and building upon existing work is the norm.  It is essential, however, that we provide proper attribution.  When in doubt, cite!  
