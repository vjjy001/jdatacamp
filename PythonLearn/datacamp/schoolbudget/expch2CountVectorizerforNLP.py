'''
Creating a bag-of-words in scikit-learn
In this exercise, you'll study the effects of tokenizing in different ways by comparing the bag-of-words representations resulting from different token patterns.

You will focus on one feature only, the Position_Extra column, which describes any additional information not captured by the Position_Type label.

For example, in the Shell you can check out the budget item in row 8960 of the data using df.loc[8960]. Looking at the output reveals that this Object_Description is overtime pay. For who? The Position Type is merely "other", but the Position Extra elaborates: "BUS DRIVER". Explore the column further to see more instances. It has a lot of NaN values.

Your task is to turn the raw text in this column into a bag-of-words representation by creating tokes that contain only alphanumeric characters.

For comparison purposes, the first 15 tokens of vec_basic, which splits df.Position_Extra into tokens when it encounters only whitespace characters, have been printed along with the length of the representation.
'''

# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create the token pattern: TOKENS_ALPHANUMERIC
TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

# Fill missing values in df.Position_Extra
df.Position_Extra.fillna('',inplace=True)

# Instantiate the CountVectorizer: vec_alphanumeric
vec_alphanumeric = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC)

# Fit to the data
vec_alphanumeric.fit(df.Position_Extra)

# Print the number of tokens and first 15 tokens
msg = "There are {} tokens in Position_Extra if we split on non-alpha numeric"
print(msg.format(len(vec_alphanumeric.get_feature_names())))
print(vec_alphanumeric.get_feature_names()[:15])
'''

198                                   
209                                   
750                            TEACHER
931                                   
1524                                  
1770                                  
1951                                  
2542        PROFESSIONAL-INSTRUCTIONAL
2640                                  
2939                      UNDESIGNATED
3029                      UNDESIGNATED
3395        PROFESSIONAL-INSTRUCTIONAL
4490                      UNDESIGNATED
4593        PROFESSIONAL-INSTRUCTIONAL
5050        PROFESSIONAL-INSTRUCTIONAL
5066                                  
5370                PROFESSIONAL-OTHER
5916                                  
6029               TIME CARD CERTIFIED
6054             ATHLETIC OPTIONAL PAY
6730                                  
6794                                  
7041                              AIDE
7151        PROFESSIONAL-INSTRUCTIONAL
8384                                  
8468                                  
8815                                  
8960                        BUS DRIVER
9722                                  
10876                   TEACHER MASTER
                      ...             
444647                TEACHER BACHELOR
444719                                
444808              PROFESSIONAL-OTHER
445206                                
445678                                
445947                PARAPROFESSIONAL
445981                    UNDESIGNATED
446032                   ADMINISTRATOR
446102                                
446199                    UNDESIGNATED
446528                   ADMINISTRATOR
446628                   ADMINISTRATOR
446668                                
447383      PROFESSIONAL-INSTRUCTIONAL
447387                                
447492                                
447887                                
448122     ANY CUS WHO IS NOT A SUPER 
448298                    UNDESIGNATED
448628                                
448733                                
448959    CONTRACTUAL SERVICES - OTHER
449761                                
450067                    UNDESIGNATED
450277                                
344986      PROFESSIONAL-INSTRUCTIONAL
384803      PROFESSIONAL-INSTRUCTIONAL
224382                                
305347     ANY CUS WHO IS NOT A SUPER 
101861      PROFESSIONAL-INSTRUCTIONAL

'''
'''
There are 123 tokens in Position_Extra if we split on non-alpha numeric
['1st', '2nd', '3rd', 'a', 'ab', 'additional', 'adm', 'administrative', 'and', 'any', 'art', 'assessment', 'assistant', 'asst', 'athletic']
'''