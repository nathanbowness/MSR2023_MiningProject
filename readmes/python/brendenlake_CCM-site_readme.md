# Computational cognitive modeling - Spring 2022

**Instructor**: [Brenden Lake](https://cims.nyu.edu/~brenden/)

**Teaching Assistants**: Yanli Zhou and [Guy Davidson](https://guydavidson.me/)

**Meeting time and location**:  
**Lecture.** Our course will use a "flipped classroom" model. Lectures will be pre-recorded and available to watch on Vimeo (password on EdStem), which is followed by a live discussion of the material in person (or on zoom). Please watch the lecture *before* the date it is listed under, so that we have a productive live discussion. Please come ready with your questions.  
Live discussion of the lectures is on **Mondays 10-11 AM**. You can attend in person at 60 5th Ave Room 150. There is also a zoom option (links available on the class brightspace and EdStem). 

**Labs.** 
Tuesdays 1:30-2:20 PM. You can attend in person at the Silver Center Room 520 or on zoom (links available on class brightspace and Edstem).

**Brightspace access for waitlist and auditors.** You shouldn't need brightspace access unless you want to watch cloud recordings (everything else is on Edstem or this website). If you do want access, please add your email to this [spreadsheet](https://docs.google.com/spreadsheets/d/12xuNgQ17GiTM6W4GulXkqF78kbR8qX-MFooYcPksUQ0/edit?usp=sharing). We will add the emails from the spreadsheet periodically.

**Course numbers**:  
DS-GA 1016 (Data Science)  
PSYCH-GA 3405.004 (Psychology)  

**Contact information and EdStem**:  
EdStem is the main point of contact. We use EdStem for questions and class discussion. Rather than emailing questions to the teaching staff, please post your questions on EdStem. It will get you a faster response and the answer will benefit others with the same question.

The signup link for our EdStem page is available here ([https://edstem.org/us/join/KPspc2](https://edstem.org/us/join/KPspc2)).

Once signed up, our class EdStem page is available here ([https://edstem.org/us/courses/18607/discussion/](https://edstem.org/us/courses/18607/discussion/)).



If you have a question that isn't suitable for EdStem and there is a need to email the teaching staff directly, please use the following email address: **instructors-ccm-spring2022@googlegroups.com**

**Office hours (via Zoom. Look for links in pinned post on EdStem)**:    
Brenden Lake (Wed 4:30-5:30 PM)  
Yanli Zhou (Thursday 2:30-3:30 PM)  
Guy Davidson (Tuesday 12-1 PM)

**Summary**: This course surveys the leading computational frameworks for understanding human intelligence and cognition. Both psychologists and data scientists are working with increasingly large quantities of human behavioral data. Computational cognitive modeling aims to understand behavioral data and the mind and brain, more generally, by building computational models of the cognitive processes that produce the data. This course introduces the goals, philosophy, and technical concepts behind computational cognitive modeling.

The lectures cover artificial neural networks (deep learning), reinforcement learning, Bayesian modeling, model comparison and fitting, classification, probabilistic graphical models, and program induction. Modeling examples span a broad set of psychological abilities including learning, categorization, language, memory, decision making, and reasoning. The homework assignments include examining and implementing the models surveyed in class. Students will leave the course with a richer understanding of how computational modeling advances cognitive science, how cognitive science can inform research in machine learning and AI, and how to fit and evaluate cognitive models to understand behavioral data.

Please note that this syllabus is not final and there may be further adjustments.

## Pre-requisites
- Math: We will use concepts from linear algebra, calculus, and probability. If you had linear algebra and calculus as an undergrad, or if you have taken Math Tools in the psychology department, you will be in a good position for approaching the material. Familiarity with probability is also assumed. We will review some of the basic technical concepts in lab.

- Programming: Previous experience with Python is required. Previous IN CLASS experience with Python is strongly recommend---it’s assumed you know how to program in Python. The assignments will use Python 3 and Jupyter Notebooks (http://jupyter.org)

## Grading
The final grade is based on the homeworks (65%) and the final project (35%).   

Class participation may be used to decide grades in borderline cases.   

## Final Project
The final project proposal is due April 11 (0.5 pages written). Please submit via email to instructors-ccm-spring2022@googlegroups.com with the file name lastname1-lastname2-lastname3-ccm-proposal.pdf. Make sure to include the names of all of your group members at the top of the document too.

The final project is due May 11. Please submit via email to instructors-ccm-spring2022@googlegroups.com with the file name lastname1-lastname2-lastname3-ccm-final.pdf. Make sure to include the names of all of your group members at the top of the document too.

The final project will be done in groups of 3-4 students. A short paper will be turned in describing the project (approximately 6 pages). The project will represent either an substantial extension of one of the homeworks (e.g., exploring some new aspect of one of the assignments), implementing and extending an existing cognitive modeling paper, or a cognitive modeling project related to your research.  We provide a list of project ideas [here](final_project_ideas.md), but of course you do not have to choose from this list.

**The final project must relate to computational cognitive modeling and cannot be a purely machine learning / data science project.** Thus, your project must connect, in some way, to the human mind and behavior. This could be collecting (informally) behavioral data to compare your computational model to. Or you could compare your model against results in the literature or particular dataset of human behavior or ratings. Or you could compare your algorithm with human intelligence in a more abstract sense. There are many ways to make the connection, but your final project must connect to computational cognitive modeling.

Write-ups should be organized and written as a scientific paper. It must include the following sections: Introduction (with review of related work), Methods/Models, Results, and Discussion/Conclusion. A good example would be to follow the structure of this paper from the class readings:
- Peterson, J., Abbott, J., & Griffiths, T. (2016). Adapting Deep Network Features to Capture Psychological Representations. Presented at the 38th Annual Conference of the Cognitive Science Society. [link here](https://arxiv.org/abs/1608.02164)

Code submission is not required for the final project.

## Lecture schedule
Live discussion is on Mondays 10-11 AM. Pre-recorded lectures both from Brenden Lake and [Todd Gureckis](https://as.nyu.edu/faculty/todd-gureckis.html).

- Mon. Jan 24: Introduction
 ([video](https://vimeo.com/666970843))([slides-intro](slides/lecture-01-introduction.pdf)([slides-logistics](slides/lecture-00-logistics.pdf))
- Mon. Jan 31: Neural networks / Deep learning (part 1)([video](https://vimeo.com/669931315))([slides](slides/lecture-02-neural_nets.pdf))
  - Homework 1 assigned (Due 2/14) (instructions for accessing [here](retrieving_hw.md))
- Mon. Feb. 7: Neural networks / Deep learning (part 2)([video](https://vimeo.com/672863803))([slides](slides/lecture-03-neural_nets.pdf))
- Mon. Feb. 14: Reinforcement learning (part 1)([video](https://vimeo.com/674866440))([slides](slides/lecture-04-reinforcementlearning.pdf))
- Mon. Feb. 21: No class, Presidents' Day
- Mon. Feb. 28: Reinforcement learning (part 2)([video](https://vimeo.com/679717285))([slides](slides/lecture-05-reinforcementlearning.pdf))
  - Homework 2 assigned (Due 3/21) (instructions for accessing [here](retrieving_hw.md))
- Mon. Mar. 7: Reinforcement learning (part 3)([video](https://vimeo.com/679717912))([slides](slides/lecture-06-reinforcementlearning.pdf))
- Mon. Mar. 14: No class, Spring break
- Mon. Mar 21: Bayesian modeling (part 1)([video](https://vimeo.com/686035229))([slides](slides/lecture-07+08-bayesian_modeling.pdf))
  - Homework 3 assigned (Due 4/4) (instructions for accessing [here](retrieving_hw.md))
- Mon. Mar 28: Bayesian modeling (part 2)([video](https://vimeo.com/686035353))(same slides as part 1)
- Mon. Apr 4: Model comparison and fitting, tricks of the trade([video](https://vimeo.com/693685336))([slides](slides/lecture-09-modelfit.pdf))
- Mon. Apr 11: Categorization ([video](https://vimeo.com/693682566))([slides](slides/lecture-10-categorization.pdf))
  - Project proposal is due
  - Homework 4 assigned (Due 4/25) (instructions for accessing [here](retrieving_hw.md))
- Mon. Apr 18: Probabilistic Graphical models ([video](https://vimeo.com/698726807))([slides](slides/lecture-11-graphical_models.pdf))
- Mon. Apr 25: Information sampling and active learning ([video](https://vimeo.com/701788628))([slides](slides/lecture-12-activelearning.pdf))
- Mon May 2: Program induction and language of thought models ([video](https://vimeo.com/703333218))([slides](slides/lecture-13-program_induction.pdf))
- Mon May 9: Computational Cognitive Neuroscience([video](https://vimeo.com/706312739))([slides](slides/lecture-14-computational_cognitive_neuroscience.pdf))
- Final summary ([video](https://vimeo.com/706313158))
- Final project due (Due May 11)


## Lab schedule
Tuesdays 1:30-2:20 PM (in person or zoom)

- Tue Jan 25, Python and Jupyter notebooks review
- Tue Feb 01, Introduction to PyTorch
- Tue Feb 08, HW 1 Review
- Tue Feb 15, No lab
- Tue Feb 22, No lab
- Tue Mar 01, Reinforcement learning
- Tue Mar 08, HW 2 review
- Tues Mar 15, No lab, spring reak 
- Tue Mar 22, Probability Review
- Tue Mar 29, HW 3 Review
- Tue Apr 5, No lab
- Tue Apr 12, No lab
- Tue Apr 19, HW 4 Review
- Tue Apr 26, No lab
- Tue May 3, No lab
- Tue May 10, No lab


## Readings
For each major topic, there are assigned readings that go with the lectures.  The papers were selected to be fundamental readings on this topic any computational cognitive scientist would be expected to know.   You should aim to read these over the course of the semester, especially during the periods when we are covering the same topic. The papers should be downloadable on Google Scholar via NYU Library.  However, they are available for download on EdStem website under the "resources" tab (see the down pointing arrow along the top bar or [this link](https://edstem.org/us/courses/18607/resources)).

**Neural networks and deep learning**
- McClelland, J. L., Rumelhart, D. E., & Hinton, G. E. The Appeal of Parallel Distributed Processing. Vol I, Ch 1.
- LeCun, Y., Bengio, Y. & Hinton, G. (2015). Deep learning. Nature 521:436–44.
- McClelland, J. L., & Rogers, T. T. (2003). The parallel distributed processing approach to semantic cognition. Nature Reviews Neuroscience, 4(4), 310-322.
- Elman, J. L. (1990). Finding structure in time. Cognitive Science, 14(2), 179-211.
- Peterson, J., Abbott, J., & Griffiths, T. (2016). Adapting Deep Network Features to Capture Psychological Representations. Presented at the 38th Annual Conference of the Cognitive Science Society.

**Reinforcement learning and decision making**
- Gureckis, T.M. and Love, B.C. (2015) Reinforcement learning: A computational perspective. Oxford Handbook of Computational and Mathematical Psychology, Edited by Busemeyer, J.R., Townsend, J., Zheng, W., and Eidels, A., Oxford University Press, New York, NY.
- Daw, N.S. (2013) "Advanced Reinforcement Learning" Chapter in Neuroeconomics: Decision making and the brain, 2nd edition
- Niv, Y. and Schoenbaum, G. (2008) “Dialogues on prediction errors” Trends in Cognitive Science, 12(7), 265-72.
- Nathaniel D. Daw, John P. O'Doherty, Peter Dayan, Ben Seymour & Raymond J. Dolan (2006). Cortical substrates for exploratory decisions in humans. Nature, 441, 876-879.

**Bayesian modeling**
- Russell, S. J., and Norvig, P. Artificial Intelligence: A Modern Approach. Chapter 13, Uncertainty.
- Tenenbaum, J. B., and Griffiths, T. L. (2001). Generalization, similarity, and Bayesian inference. Behavioral and Brain Sciences, 24(4), 629-640.
- Tenenbaum, J. B., Kemp, C., Griffiths, T. L., & Goodman, N. D. (2011). How to grow a mind: Statistics, structure, and abstraction. Science, 331(6022), 1279-1285.
- Ghahramani, Z. (2015). Probabilistic machine learning and artificial intelligence. Nature, 521(7553), 452.
- MacKay, D. (2003). Chapter 29: Monte Carlo Methods. In Information Theory, Inference, and Learning Algorithms.

**Rational versus mechanistic modeling approaches**
- Jones, M. & Love, B.C. (2011). Bayesian Fundamentalism or Enlightenment? On the Explanatory Status and Theoretical Contributions of Bayesian Models of Cognition. Behavioral and Brain Sciences (target article).
- Griffiths, T.L., Lieder, F., & Goodman, N.D. (2015). Rational use of cognitive resources: Levels of analysis between the computational and the algorithmic. Topics in Cognitive Science, 7(2), 217-229.

**Model comparison and fitting, tricks of trade**
- Wilson, R.C. and Collins, A.G.E. (2019). Ten simple rules for the computational modeling of behavioral data.  eLife 2019;8:e49547
- Pitt, M.A. and Myung, J (2002) When a good fit can be bad. Trends in Cognitive Science, 6, 10, 421-425.
- Roberts, S. & Pashler, H. (2000) How persuasive is a good fit? A comment on theory testing. Psychological Review, 107, 358-367.
- \[optional\] Myung, I.J. (2003). Tutorial on maximum likelihood estimation. Journal of Mathematical Psychology, 47, 90-100.

**Probabilistic graphical models**
- Charniak (1991). Bayesian networks without tears. AI Magazine, 50-63.
- Kemp, C., & Tenenbaum, J. B. (2008). The discovery of structural form. Proceedings of the National Academy of Sciences, 105(31), 10687-10692.
- \[optional\]  Russell, S. J., and Norvig, P. Artificial Intelligence: A Modern Approach. Chapter 14, Probabilistic reasoning systems.

**Program induction and language of thought models**
- Ghahramani, Z. (2015). Probabilistic machine learning and artificial intelligence. Nature, 521(7553), 452.
- Goodman, N. D., Tenenbaum, J. B., & Gerstenberg, T. (2014). Concepts in a probabilistic language of thought. Center for
Brains, Minds and Machines (CBMM).
- Lake, B. M., Salakhutdinov, R., & Tenenbaum, J. B. (2015). Human-level concept learning through probabilistic program induction. Science, 350(6266), 1332-1338.

**Computational Cognitive Neuroscience**
- Kreigeskorte, N. and Douglas, P.K. (2018) Cognitive computational neuroscience. Nature Neuroscience. 21(9): 1148-1160. doi:10.1038/s41593-018-0210-5
- Turner, B.M., Forstmann, B.U., Love, B.C., Palmeri, T.J., Van Maanen, L. (2017). Approaches to analysis in model-based cognitive neuroscience. Journal of Mathematical Psychology. 76(B), 65-79.


## Course policies and FAQ

**Collaboration and honor code**:  
We take the collaboration policy and [academic integrity](https://cas.nyu.edu/content/nyu-as/cas/academic-integrity.html) very seriously. Violations of the policy will result in zero points and possible disciplinary referral. You may discuss the homework assignments with your classmates, but **you must run the simulations and complete the write-ups for the homeworks on your own.** Under no circumstance should students look at each other’s code or write ups, or code/write-ups from previous years of this course. Do not share your write up or code with any of your classmates under any circumstances.

**Late work**:  
We will take off 10% for each day a homework or final project is late. Assignments should be turned in all-at-once and not in pieces. If an assignment is incomplete and later completed, the late penalty is applied to the entire assignment.

**Extensions**:  
If you are requesting an extension, email the teaching team (instructors-ccm-spring2022@googlegroups.com) and explain the reason. You must submit a request for extension at least 24 hours before the due date of the assignment.

**Regrading**:  
If you feel there was a mistake in the grading of your assignment, you can formally request a regrade by emailing the teaching team. This will prompt us to regrade the entire assignment and could lead to your grade being either raised or lowered depending on what the regrade finds. You can submit a regrade request via gradescope.

**Did you forget to turn in part of the homework, or did it print improperly on the PDF?**:  
Before turning in your assignment, double check that all of your answers appear clearly in the PDF printout. We will not regrade a homework because your answer did not display correctly in the version you submitted.

**Extra credit**:  
No extra credit will be given, out of interest of fairness.

## Preconfigured cloud environment
Students registered for the course have the option of completing homework assignments on their personal computers, or in a cloud Jupyter environment with all required packages pre-installed. Students can log onto the environment using their nyu net ids [here](https://dsga-1016-spring.rcnyu.org).
