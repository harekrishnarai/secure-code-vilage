public class Factory {
    public static Object create(String className) throws Exception {
        if (!"com.example.Task".equals(className)) {
            throw new IllegalArgumentException("Unsupported class");
        }
        Class<?> clazz = Class.forName(className);
        return clazz.getDeclaredConstructor().newInstance();
    }
}
