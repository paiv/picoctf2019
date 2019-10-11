// c++ -std=c++14 -O2 eval.cpp -o eval
#include <iostream>
#include <sstream>

typedef int32_t i32;
typedef int64_t i64;

using namespace std;

enum class NodeType {
    Number,
    OpAdd,
    OpSub,
    OpMul,
};

typedef struct Node {
    NodeType type;
    i64 value;
    Node* left;
    Node* right;
} Node;


static i64
parse_int(istringstream& si) {
    i64 x;
    si >> x;
    return x;
}

static Node*
parse_node(istringstream& si) {
    Node* node = new Node;
    *node = {};

    int x = si.peek();
    while (si && isspace(x)) {
        si.seekg(1, si.cur);
        x = si.peek();
    }

    switch (x) {
    case EOF:
        break;
    case '-': case '0': case '1': case '2': case '3': case '4': case '5':
    case '6': case '7': case '8': case '9':
        node->type = NodeType::Number;
        node->value = parse_int(si);
        break;
    case '(': {
        char x, op = 0;
        si >> x;
        Node* left = parse_node(si);
        si >> op;
        switch (op) {
            case '+':
                node->type = NodeType::OpAdd; break;
            case '-':
                node->type = NodeType::OpSub; break;
            case '*':
                node->type = NodeType::OpMul; break;
            case ')':
                delete node;
                return left;
            default:
                clog << "unhandled op: " << op << " " << (int)op << endl;
                exit(1);
        }
        node->left = left;
        node->right = parse_node(si);
        }
        break;
    default:
        clog << "unexpected char: " << (char)x << endl;
        exit(1);
    }

    return node;
}

static i64
eval_node(Node* node) {
    switch (node->type) {
    case NodeType::OpAdd:
            return eval_node(node->left) + eval_node(node->right);
    case NodeType::OpSub:
        return eval_node(node->left) - eval_node(node->right);
    case NodeType::OpMul:
        return eval_node(node->left) * eval_node(node->right);
    case NodeType::Number:
        return node->value;
    }
}


int main(int argc, char const *argv[]) {
    string s;
    getline(cin, s);
    istringstream si(s);

    Node* root = parse_node(si);
    i64 x = eval_node(root);
    cout << x << endl;

    return 0;
}
