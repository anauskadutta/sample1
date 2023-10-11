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
            bool isWord;
            if(word == "hi"){

            } else {
                try
                {
                    isWord = true;
                    Console.WriteLine("It is a word!");
                    return word;
                }
                finally
                {
                    isWord = false;
                }
            }
            return null;
        }
    }
}
