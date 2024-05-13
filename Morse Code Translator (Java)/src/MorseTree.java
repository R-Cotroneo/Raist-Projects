
public class MorseTree {
	//Creating tree with getters and setters
	TreeNode<Character> myTree;
	public TreeNode<Character> getMyTree() {
		return myTree;
	}
	public void setMyTree(TreeNode<Character> myTree) {
		this.myTree = myTree;
	}
	
	//Default constructor
	public MorseTree()
	{
		this.myTree = new TreeNode<Character>(null);
	}
	
	//Provides pre order of the tree
	public String preOrder()
	{
		return myTree.preorder();
	}
	
	//Provides post order of the tree
	public String postOrder()
	{
		return myTree.postorder();
	}
		
	//Takes each letter individually for translation
	public String makeMorse(String phrase)
	{
		phrase = phrase.toLowerCase();
		String morse = "";
		for (int i = 0; i < phrase.length(); i++)
		{
			char letter = phrase.charAt(i);
			if (letter == ' ')
			{
				morse += "";
			}
			else
			{
				String morseLetter = "";
				morse += morseCreate(letter, myTree, morseLetter);
				if (i != phrase.length() - 1)
				{	
					morse += "|";
				}
			}
		}
		return morse;
	}
	
	//Searching the tree for the letter sent in from makeMorse function
	public String morseCreate(char letter, TreeNode<Character> tree, String morseLetter)
	{
		//Base case that says it failed to find the letter on this search
		if (tree.getLeft() == null && tree.getRight() == null)
		{
			morseLetter = "";
			return morseLetter;
		}
		//Assuming only a left node
		else if (tree.getLeft() != null && tree.getRight() == null)
		{
			//Finds the letter and returns it in morse
			if (tree.getLeft().getElement() == letter)
			{
				return morseLetter += "o";
			}
			//Fails to find the letter and continues search
			else
			{
				return morseCreate(letter, tree.getLeft(), morseLetter + "o");
			}
		}
		//Assuming only a right node
		else if (tree.getLeft() == null && tree.getRight() != null)
		{
			//Finds the letter and returns it in morse
			if (tree.getRight().getElement() == letter)
			{
				return morseLetter += "-";
			}
			//Fails to find the letter and continues search
			else
			{
				return morseCreate(letter, tree.getRight(), morseLetter + "-");
			}
		}
		//Has both nodes
		else
		{
			//Finds the letter on the left
			if (tree.getLeft().getElement() == letter)
			{
				morseLetter += "o";
				return morseLetter;
			}
			//Finds the letter on the right
			else if (tree.getRight().getElement() == letter)
			{
				morseLetter += "-";
				return morseLetter;
			}
			//Fails to find the letter on either side, continues search on both sides
			else
			{
				return morseCreate(letter, tree.getLeft(), morseLetter + "o") + morseCreate(letter, tree.getRight(), morseLetter + "-");
			}
		}
			
	}
	
	//Takes each morse letter individually and translates them
	String makeEnglish(String phrase)
	{
		String englishPhrase = "";
		String morseLetter = "";
		char letter;
		for (int i = 0; i < phrase.length(); i++)
		{
			if (phrase.charAt(i) != '|')
			{
				morseLetter += phrase.charAt(i);
				if (i == phrase.length() - 1)
				{
					letter = englishCreate(morseLetter, myTree);
					englishPhrase += letter;
				}
			}
			else
			{
				letter = englishCreate(morseLetter, myTree);
				englishPhrase += letter;
				morseLetter = "";
			}
		}
		return englishPhrase;
	}
	
	//Searches for the letter to be returned
	char englishCreate(String morse, TreeNode<Character> tree)
	{
		//Letter in the left descendant
		if (morse.length() == 1 && morse.charAt(0) == 'o')
		{
			return tree.getLeft().getElement();
		}
		//Letter in the right descendant
		else if (morse.length() == 1 && morse.charAt(0) == '-')
		{
			return tree.getRight().getElement();
		}
		//Searches down the left side
		else if (morse.charAt(0) == 'o')
		{
			return englishCreate(morse.substring(1), tree.getLeft());
		}
		//Searches down the right side
		else if (morse.charAt(0) == '-')
		{
			return englishCreate(morse.substring(1), tree.getRight());
		}
		//Failure to translate
		else
		{
			return '1';
		}
	}
}
