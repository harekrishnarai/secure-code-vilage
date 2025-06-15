public class Factory {
    public static Object create(String className) throws Exception {
        Class<?> clazz = Class.forName(className);
        return clazz.newInstance();
    }
}
