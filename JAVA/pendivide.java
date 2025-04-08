public class pendivide {
    public static void main(String[] args){
        int pens = 14;
        int students = 3;
        int pensPerStudent = pens / students;
        int pensremaining = pens % students;
        System.out.println("Each student gets " + pensPerStudent + " pens.");
        System.out.println("There are " + pensremaining + " pens left over.");
    } 
}