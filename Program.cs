namespace sample1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            String word = FindWord("byee");
            Console.WriteLine(word);
        }

        public static String FindWord(String word){
            bool isWord;
            if(word == "hi"){

            } else {
                try
                {
                    Console.WriteLine("It is a word!");
                    return word;
                }
                finally
                {}
            }
            return null;
        }
    }
}
