### Algorithm

The algorithm consists of the following steps:
1. **Loading and processing data**
  <br />The classes are loaded from the JSON file and are allocated to the appropriate structures. 
2. **Model setting**
    1. *Class*
        <br/> It contains class name, class teachers, class timings,(List of) Classrooms available and (List of)Student Groups who are enrolled in this class.
    2. *Classroom*
    <br/> It contains the classroom name, and it's type.

  <br />Creation of schedule matrix and dictionaries representing empty fields, filled fields in a matrix, order of classes for each type of class and group, an empty group idle, and an empty teacher's idle.
3. **Generating the initial population**
  <br />Classes are arranged in vertically consecutive blank spaces of the matrix so that they are in the appropriate classroom.
4. **(1 + 1) evolution strategy for hard constraints**
  <br />The selection of classes that change the place in the schedule is based on the cost of the classes calculating only the hard constraints. Classes with the highest cost are chosen and with a certain probability mutated. Mutation is changing the field in the matrix by looking for a free field that meets all the rigid constraints. Schwefel's notation is also used.
5. **Simulated hardening for additional criteria**
  <br />Optimizes the previously generated schedule by minimizing the idle time for groups for all days and the existence of free hour in which there is no teaching. In each iteration, a random number of classes are mututed, i.e. they change the place in the matrix so they continue to meet hard constraints. For the cooling schedule, a geometric temperature drop is used.
