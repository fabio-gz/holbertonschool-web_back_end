const getStudentsByLocation = (students, city) => (
  students.filter((stds) => stds.location === city)
);

export default getStudentsByLocation;
