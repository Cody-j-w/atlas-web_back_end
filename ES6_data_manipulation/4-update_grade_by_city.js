export default function updateStudentGradeByCity(arr, city, newGrades) {
  // filter list of students by city
  const filteredStudents = arr.filter((student) => student.location === city);

  // map filtered student list to new list, adding grades to each student
  const gradedStudents = filteredStudents.map((student) => {
    // filter out the correct grade
    const studentGrade = newGrades.filter((grade) => grade.studentId === student.id);

    // if the correct filter has been found for the student, assign it - otherwise, assign 'N/A'
    if (studentGrade.length !== 0) {
      Object.assign(student, { grade: studentGrade[0].grade });
    } else {
      Object.assign(student, { grade: 'N/A' });
    }
    // return the graded student
    return student;
  });
  return gradedStudents;
}
