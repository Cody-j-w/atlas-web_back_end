/* eslint-diable no-unused-vars */
export default function createReportObject(employeesList) {
  const employeesObj = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employeesList) {
      let count = 0;
      for (const department in employeesList) {
        count += 1;
      }
      return count;
    },
  };
  return employeesObj;
}
