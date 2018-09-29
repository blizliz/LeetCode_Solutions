class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {

        if (words.size() == 1) {
            return 1;
        }

        map<char, string> morse = {{'a', ".-"},
                                   {'b', "-..."},
                                   {'c', "-.-."},
                                   {'d', "-.."},
                                   {'e', "."},
                                   {'f', "..-."},
                                   {'g', "--."},
                                   {'h', "...."},
                                   {'i', ".."},
                                   {'j', ".---"},
                                   {'k', "-.-"},
                                   {'l', ".-.."},
                                   {'m', "--"},
                                   {'n', "-."},
                                   {'o', "---"},
                                   {'p', ".--."},
                                   {'q', "--.-"},
                                   {'r', ".-."},
                                   {'s', "..."},
                                   {'t', "-"},
                                   {'u', "..-"},
                                   {'v', "...-"},
                                   {'w', ".--"},
                                   {'x', "-..-"},
                                   {'y', "-.--"},
                                   {'z', "--.."}};

        //transformation:

        set<string> trans;

        for (int16_t i = 0; i < words.size(); ++i) {
            string strMorse;
            for (int16_t j = 0; j < words[i].size(); ++j) {
                strMorse += morse[words[i][j]];
            }
            trans.insert(strMorse);
            strMorse.clear();
        }

        //solution:

        return trans.size();
    }
};