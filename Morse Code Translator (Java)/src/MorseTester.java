
public class MorseTester {

	//Function for creating the morse tree
	public static void insertLetters(TreeNode<Character> tree)
	{
		tree.setElement('_');
		tree.insertLeft('e');
		tree.insertRight('t');
		tree.getLeft().insertLeft('i');
		tree.getLeft().insertRight('a');
		tree.getRight().insertLeft('n');
		tree.getRight().insertRight('m');
		tree.getLeft().getLeft().insertLeft('s');
		tree.getLeft().getLeft().insertRight('u');
		tree.getLeft().getRight().insertLeft('r');
		tree.getLeft().getRight().insertRight('w');
		tree.getRight().getLeft().insertLeft('d');
		tree.getRight().getLeft().insertRight('k');
		tree.getRight().getRight().insertLeft('g');
		tree.getRight().getRight().insertRight('o');
		tree.getLeft().getLeft().getLeft().insertLeft('h');
		tree.getLeft().getLeft().getLeft().insertRight('v');
		tree.getLeft().getLeft().getRight().insertLeft('f');
		tree.getLeft().getRight().getLeft().insertLeft('l');
		tree.getLeft().getRight().getRight().insertLeft('p');
		tree.getLeft().getRight().getRight().insertRight('j');
		tree.getRight().getLeft().getLeft().insertLeft('b');
		tree.getRight().getLeft().getLeft().insertRight('x');
		tree.getRight().getLeft().getRight().insertLeft('c');
		tree.getRight().getLeft().getRight().insertRight('y');
		tree.getRight().getRight().getLeft().insertLeft('z');
		tree.getRight().getRight().getLeft().insertRight('q');
	}
	
	
	public static void main(String[] args){
		//Creating the tree
		MorseTree codeTree = new MorseTree();
		codeTree.myTree.setElement('_');
		insertLetters(codeTree.myTree);
		
		//Printing pre/post order
		System.out.println(codeTree.preOrder());
		System.out.println(codeTree.postOrder());
		
		//Translating from English to morse
		String englishPhrase = "Science compels us to explode the sun";
		System.out.println(englishPhrase);
		
		String morsePhrase = codeTree.makeMorse(englishPhrase);
		System.out.println(morsePhrase);
		
		//Translating from morse to English
		String newEnglish = codeTree.makeEnglish(morsePhrase);
		System.out.println(newEnglish);
		
	}

}
