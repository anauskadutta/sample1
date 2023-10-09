namespace sample1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            String word = FindWord("hello");
            Console.WriteLine(word);
        }

        public static String FindWord(String word){
            String password = "abcd123";
            Console.WriteLine(password);
            if(word == "hi")
                return word;
            return null;
        }
    }
}
