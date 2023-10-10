namespace sample1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            String word = FindWord("bye");
            Console.WriteLine(word);
        }

        public static String FindWord(String word){
            if(word == "hi"){

            }
            else
                return word;
            return null;
        }
    }
}
