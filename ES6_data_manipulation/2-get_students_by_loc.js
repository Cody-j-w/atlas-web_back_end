export default function getStudentsByLocation(arr, city) {
    if (Array.isArray(arr)) {
        return arr.filter((student) => student.location === city);
    }
}