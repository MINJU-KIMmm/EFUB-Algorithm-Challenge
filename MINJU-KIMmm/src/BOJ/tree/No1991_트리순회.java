package BOJ.tree;

import java.util.*;
import java.io.*;
public class No1991_트리순회 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        Tree tree=new Tree();

        for(int i=0;i<N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            char root=st.nextToken().charAt(0);
            char left=st.nextToken().charAt(0);
            char right=st.nextToken().charAt(0);

            tree.createNode(root, left, right);
        }

        tree.preOrder(tree.root);
        System.out.println();
        tree.inOrder(tree.root);
        System.out.println();
        tree.postOrder(tree.root);
    }


}

class Tree{
    public Node root;
    public void createNode(char data, char leftData, char rightData){
        //새로 만들 node가 root인 경우
        if(root==null){
           root=new Node(data);
           root.left=leftData!='.'?new Node(leftData):null;
           root.right=rightData!='.'?new Node(rightData):null;
        }
        //새로 만들 node가 root가 아닌 경우
        else{
            searchNode(root, data, leftData, rightData);
        }
    }

    public void searchNode(Node node, char data, char leftData, char rightData){
        if(node==null){
            return;
        }else if(node.data==data){
            node.left=leftData!='.'?new Node(leftData):null;
            node.right=rightData!='.'?new Node(rightData):null;
        }else{
            searchNode(node.left, data, leftData, rightData);
            searchNode(node.right, data, leftData, rightData);
        }
    }

    //전위순회
    //root -> left -> right
    public void preOrder(Node node){
        if(node!=null){
            System.out.print(node.data);
            if(node.left!=null) preOrder(node.left);
            if(node.right!=null) preOrder(node.right);
        }
    }

    //중위 순회
    // left -> root -> right
    public void inOrder(Node node){
        if(node!=null){
            if(node.left!=null) inOrder(node.left);
            System.out.print(node.data);
            if(node.right!=null) inOrder(node.right);
        }
    }

    //후위순회
    //left -> right ->  root
    public void postOrder(Node node){
        if(node!=null){
            if(node.left!=null) postOrder(node.left);
            if(node.right!=null) postOrder(node.right);
            System.out.print(node.data);
        }
    }


}
class Node{
    char data;
    Node left;
    Node right;

    Node(char data){
        this.data=data;
    }
}