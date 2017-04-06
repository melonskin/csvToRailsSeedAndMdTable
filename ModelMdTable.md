#### User


|name |email |password |password_confirmation |
|:---|:---|:---|:---|
|Johana  |xxx@tamu.edu |aaaaaa |aaaaaa |
|Yining |yyy@tamu.edu |aaaaaa |aaaaaa |
|Andres |xxx2@tamu.edu |aaaaaa |aaaaaa |
|Shijin |yyy1@tamu.edu |aaaaaa |aaaaaa |
|Jingjia |xxx3@tamu.edu |aaaaaa |aaaaaa |


#### Student


|firstname |lastname |is_f1 |program_id |user_id |yearstart |semstart |yearend |semend |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|Johana  |Rueda |FALSE |1 |1 |2017 |Spring |2019 |Spring |
|Yining |Bao |TRUE |2 |2 |2017 |Fall |2019 |Fall |
|Andres |Gonzalez |TRUE |3 |3 |2018 |Spring |2019 |Fall |
|Shijin |Tang |TRUE |4 |4 |2018 |Fall |2020 |Fall |
|Jingjia |Li |FALSE |1 |5 |2019 |Spring |2022 |Spring |


#### Program


|name |acronym |is_thesis |dep_hour |graded_grad_hour |ug_class |non_dep_hour_min |non_dep_hour_max |seminar_hour_min |seminar_hour_max |direct_study_hour_min |direct_study_hour_max |total_hour |total_hour_prior |research_hour_min |research_hour_max |joint_hour_min |joint_hour_max |elective_hour_min |elective_hour_max |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|Master of Computer Science |MCS |FALSE |18 |0 |1 |0 |6 |1 |1 |0 |3 |30 |0 |0 |0 |0 |0 |0 |0 |
|Master of Engineering in Computer Science |MEN |FALSE |12 |0 |1 |0 |999 |1 |1 |0 |3 |30 |0 |4 |7 |6 |999 |6 |999 |
|Master of Science in Computer Science |MSCS |TRUE |18 |0 |1 |0 |6 |1 |1 |0 |3 |32 |0 |4 |7 |0 |0 |0 |0 |
|Master of Science in Computer Engineering |MSCE |TRUE |10 |0 |1 |0 |999 |1 |1 |0 |3 |32 |0 |4 |7 |6 |999 |6 |999 |
|PhD in Computer Science |PhDCS |TRUE |30 |0 |0 |0 |6 |1 |2 |0 |0 |96 |64 |18 |999 |0 |0 |0 |0 |
|PhD in Computer Engineering |PhDCE |TRUE |12 |30 |0 |0 |999 |1 |2 |0 |0 |96 |64 |18 |999 |6 |999 |12 |999 |


#### Package


|name |no_required |program_id |
|:---|:---|:---|
|Theory |1 |1 |
|Systems |2 |1 |
|Software |1 |1 |
|Theory |1 |3 |
|Systems |1 |3 |
|Software |1 |3 |
|Theory |1 |5 |
|Systems |1 |5 |
|Software |1 |5 |


#### Semester


|term |year |
|:---|:---|
|Spring |2017 |
|Summer |2017 |
|Fall |2017 |
|Spring |2018 |
|Summer |2018 |
|Fall |2018 |
|Spring |2019 |
|Summer |2019 |
|Fall |2019 |
|Spring |2020 |
|Summer |2020 |
|Fall |2020 |
|Spring |2021 |
|Summer |2021 |
|Fall |2021 |


#### Course


|department |number |name |credit |description |is_fall |is_spring |is_summer |
|:---|:---|:---|:---|:---|:---|:---|:---|
|CSCE |603 |Database Systems and Applications |3 |Prerequisites: CSCE 601; graduate classification. |FALSE |TRUE |FALSE |
|CSCE |604 |Programming Languages |3 |Prerequisite: Graduate classification. |TRUE |FALSE |FALSE |
|CSCE |605 |Compiler Design |3 |Prerequisite: CSCE 434. |FALSE |TRUE |FALSE |
|CSCE |606 |Software Engineering |3 |Prerequisite: CSCE 431 or approval of instructor. |TRUE |TRUE |FALSE |
|CSCE |608 |Database Systems |3 |Prerequisite: CSCE 310 or CSCE 603. |TRUE |FALSE |FALSE |
|CSCE |611 |Operating Systems and Applications |3 |Prerequisites: CSCE 313; graduate classification. |TRUE |TRUE |FALSE |
|CSCE |613 |Operating Systems |3 |Prerequisite: CSCE 313 or CSCE 611. |FALSE |TRUE |FALSE |
|CSCE |614 |Computer Architecture |3 |Prerequisite: CSCE 350/ECEN 350/ECEN 350/CSCE 350. |TRUE |TRUE |FALSE |
|CSCE |617 |Co-Design of Embedded Systems (CODES) |3 |Prerequisites: CSCE 462 or equivalent, CSCE 410 and graduate classification. |TRUE |TRUE |FALSE |
|CSCE |622 |Generic Programming |3 |Prerequisite: CSCE 221. |TRUE |TRUE |FALSE |
|CSCE |624 |Sketch Recognition |3 |Prerequisite: Graduate classification. |TRUE |TRUE |FALSE |


#### Coursesection


|Department |number |Section |Instructor |Term |Year |GPA |student |A |B |C |D |F |Q |course_id |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|CSCE |603 |600 |JIANG A |Spring |2013 |4 |17 |100.00% |0.00% |0.00% |0.00% |0.00% |0.00% |1 |
|CSCE |603 |600 |JIANG A |Spring |2014 |4 |29 |100.00% |0.00% |0.00% |0.00% |0.00% |0.00% |1 |
|CSCE |604 |600 |JARVI J |Fall |2014 |3.542 |24 |54.17% |45.83% |0.00% |0.00% |0.00% |4.17% |2 |
|CSCE |604 |600 |JARVI J |Fall |2015 |3.714 |7 |85.71% |0.00% |14.29% |0.00% |0.00% |0.00% |2 |
|CSCE |605 |600 |RAUCHWERGER L |Spring |2013 |3.667 |6 |66.67% |33.33% |0.00% |0.00% |0.00% |0.00% |3 |
|CSCE |605 |600 |RAUCHWERGER L |Spring |2015 |3.556 |9 |66.67% |22.22% |11.11% |0.00% |0.00% |11.11% |3 |
|CSCE |606 |600 |WALKER D |Fall |2013 |3.951 |102 |98.04% |0.98% |0.00% |0.00% |0.98% |0.00% |4 |
|CSCE |606 |600 |WALKER D |Fall |2014 |3.83 |100 |84.00% |15.00% |1.00% |0.00% |0.00% |0.00% |4 |
|CSCE |606 |600 |HUANG S |Fall |2015 |3.953 |85 |95.29% |4.71% |0.00% |0.00% |0.00% |0.00% |4 |
|CSCE |606 |600 |WALKER D |Spring |2015 |4 |57 |100.00% |0.00% |0.00% |0.00% |0.00% |0.00% |4 |
|CSCE |606 |600 |WALKER D |Spring |2016 |3.603 |73 |61.64% |36.99% |1.37% |0.00% |0.00% |0.00% |4 |
|CSCE |608 |600 |JIANG A |Fall |2013 |3.986 |74 |98.65% |1.35% |0.00% |0.00% |0.00% |0.00% |5 |
|CSCE |608 |600 |JIANG A |Fall |2014 |3.429 |98 |42.86% |57.14% |0.00% |0.00% |0.00% |1.02% |5 |
|CSCE |608 |600 |CHEN J |Fall |2015 |3.259 |58 |31.03% |63.79% |5.17% |0.00% |0.00% |0.00% |5 |
|CSCE |611 |600 |LEYK T |Fall |2014 |3.81 |21 |85.71% |9.52% |4.76% |0.00% |0.00% |0.00% |6 |
|CSCE |611 |500 |BETTATI R |Spring |2014 |3.556 |18 |55.56% |44.44% |0.00% |0.00% |0.00% |11.11% |6 |
|CSCE |611 |600 |DA S |Fall |2015 |3.956 |23 |95.65% |4.35% |0.00% |0.00% |0.00% |4.35% |6 |
|CSCE |613 |600 |BETTATI R |Spring |2013 |3.308 |26 |61.54% |15.38% |15.38% |7.69% |0.00% |3.85% |7 |
|CSCE |613 |600 |STOLERU R |Spring |2014 |3.615 |39 |64.10% |33.33% |2.56% |0.00% |0.00% |0.00% |7 |
|CSCE |613 |600 |JIMENEZ D |Spring |2015 |3.958 |24 |95.83% |4.17% |0.00% |0.00% |0.00% |0.00% |7 |
|CSCE |613 |600 |DA S |Spring |2016 |3.564 |39 |64.10% |28.21% |7.69% |0.00% |0.00% |0.00% |7 |
|CSCE |614 |600 |KIM E |Fall |2013 |3.438 |48 |50.00% |43.75% |6.25% |0.00% |0.00% |2.08% |8 |
|CSCE |614 |600 |TAYLOR V |Spring |2013 |3.704 |27 |74.07% |22.22% |3.70% |0.00% |0.00% |0.00% |8 |
|CSCE |614 |600 |KIM E |Fall |2014 |3.328 |61 |39.34% |54.10% |6.56% |0.00% |0.00% |6.56% |8 |
|CSCE |614 |600 |JIMENEZ D |Spring |2014 |3.081 |37 |37.84% |40.54% |16.22% |2.70% |2.70% |13.51% |8 |
|CSCE |614 |600 |JIMENEZ D |Fall |2015 |3.744 |39 |79.49% |17.95% |0.00% |2.56% |0.00% |2.56% |8 |
|CSCE |614 |600 |KIM E |Spring |2015 |3.538 |52 |55.77% |42.31% |1.92% |0.00% |0.00% |5.77% |8 |
|CSCE |614 |600 |KIM E |Spring |2016 |3.538 |52 |65.38% |23.08% |11.54% |0.00% |0.00% |1.92% |8 |
|CSCE |617 |601 |MAHAPATRA R |Fall |2013 |3.375 |8 |50.00% |37.50% |12.50% |0.00% |0.00% |0.00% |9 |
|CSCE |617 |600 |MAHAPATRA R |Spring |2013 |3.833 |12 |83.33% |16.67% |0.00% |0.00% |0.00% |0.00% |9 |
|CSCE |617 |601 |MAHAPATRA R |Fall |2014 |3.714 |14 |71.43% |28.57% |0.00% |0.00% |0.00% |0.00% |9 |
|CSCE |617 |601 |MAHAPATRA R |Fall |2015 |3.867 |15 |86.67% |13.33% |0.00% |0.00% |0.00% |0.00% |9 |
|CSCE |622 |600 |STROUSTRUP B |Spring |2013 |3.379 |29 |51.72% |34.48% |13.79% |0.00% |0.00% |0.00% |10 |
|CSCE |622 |600 |JARVI J |Fall |2015 |3.926 |27 |92.59% |7.41% |0.00% |0.00% |0.00% |0.00% |10 |
|CSCE |624 |600 |HAMMOND T |Spring |2013 |3.5 |22 |59.09% |31.82% |9.09% |0.00% |0.00% |0.00% |11 |
|CSCE |624 |600 |HAMMOND T |Fall |2014 |3.958 |24 |95.83% |4.17% |0.00% |0.00% |0.00% |0.00% |11 |
|CSCE |624 |600 |HAMMOND T |Fall |2015 |3.76 |25 |84.00% |8.00% |8.00% |0.00% |0.00% |0.00% |11 |


#### PackageCourseship


|course_id |package_id |
|:---|:---|
|1 |1 |
|2 |1 |
|3 |2 |
|4 |2 |
|5 |2 |
|6 |3 |
|7 |3 |
|8 |3 |
|1 |4 |
|2 |4 |
|3 |5 |
|4 |5 |
|5 |5 |
|6 |6 |
|7 |6 |
|8 |6 |
|1 |7 |
|2 |7 |
|3 |8 |
|4 |8 |
|5 |8 |
|6 |9 |
|7 |9 |
|8 |9 |


#### StudentCourseSemestership


|student_id |course_id |semester_id |
|:---|:---|:---|
|1 |6 |1 |
|1 |4 |1 |
|1 |1 |2 |
|2 |6 |1 |
|3 |4 |1 |
|4 |1 |2 |
|5 |1 |2 |
