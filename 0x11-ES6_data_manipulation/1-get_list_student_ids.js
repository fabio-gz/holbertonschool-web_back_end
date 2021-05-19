const getListStudentsIds = (students) => {
  if (Array.isArray(students)) {
    return students.map((stds) => stds.id);
  }

  return [];
};

export default getListStudentsIds;
