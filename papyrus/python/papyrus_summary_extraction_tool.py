# -*- coding: utf-8 -*-
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import networkx as nx

#To import the above, install these in your application:

#pip install scikit-learn
#pip install numpy
#pip install scipy
#pip install networkx

#Taken from the user's uploaded PDF or URL, cleaned and formatted.
title = ''

#Taken from the user's uploaded PDF or URL, cleaned and formatted.
#This only includes the text from the body (not text in footnotes, contents, etc).

content = """

"""

paragraphs = content.split('\n\n')

#function_1: Quite simple, but effective in extracting useful info buried in hundreds of pages.
#Much thought went into the textual features that indicate or lead to useful information.
#Below is not the most elegant way to script this, lol. I'm not a good programmer. 
#Nevertheless, this has been tested with 30 different random Senate Estimates and gov speeches.

#function_2: This is a quick last-min implementation, but with more time will extend/build on this to detect discussions around issues/challenges, in particular,
#and place a higher score on these types of discussions. This is used for discussion-led documents rather than extracting facts and figures. 
#Adapted from https://joshbohde.com/blog/document-summarization

def function_1():
	summary = []
	for i in paragraphs:
		#This finds each regex and counts the number of times it occurs in the paragraph. We'll use this to sum the weights of each regex.
		count_1 = len(re.findall('\$.*?million', i)) #Dollar figure (big figures, not small expenditure)
		count_2 = len(re.findall('\$.*?billion', i)) #Dollar figure
		count_3 = len(re.findall('\$.*?m', i)) #Dollar figure
		count_4 = len(re.findall('\$.*?bn', i)) #Dollar figure
		count_5 = len(re.findall('[2][0][1-9][0-9]', i)) #4-digits that indicate a year from 2011 to 2099
		count_6 = len(re.findall('\%', i)) #Percentage
		count_7 = len(re.findall('per cent', i)) #Percentage
		count_8 = len(re.findall('percent', i)) #Percentage
		count_9 = len(re.findall('completed', i)) #Cue word
		count_10 = len(re.findall('complete', i)) #Cue word
		count_11 = len(re.findall('completing', i)) #Cue word
		count_12 = len(re.findall('implement', i)) #Cue word
		count_13 = len(re.findall('implementing', i)) #Cue word
		count_14 = len(re.findall('due', i)) #Cue word
		count_15 = len(re.findall('commence', i)) #Cue word
		count_16 = len(re.findall('begin work', i)) #Cue word
		count_17 = len(re.findall('invested', i)) #Cue word
		count_18 = len(re.findall('investing', i)) #Cue word
		count_19 = len(re.findall('invest', i)) #Cue word
		count_20 = len(re.findall('surplus', i)) #Keyword
		count_21 = len(re.findall('budget', i)) #Keyword
		count_22 = len(re.findall('plan', i)) #Cue word
		count_23 = len(re.findall('planning', i)) #Cue word
		sum_1 = 1.2 * count_1
		sum_2 = 1.2 * count_2
		sum_3 = 1.2 * count_3
		sum_4 = 1.2 * count_4
		sum_5 = 0.8 * count_5
		sum_6 = 0.6 * count_6
		sum_7 = 0.6 * count_7
		sum_8 = 0.6 * count_8
		sum_9 = 0.5 * count_9
		sum_10 = 0.5 * count_10
		sum_11 = 0.5 * count_11
		sum_12 = 0.5 * count_12
		sum_13 = 0.5 * count_13
		sum_14 = 0.5 * count_14
		sum_15 = 0.5 * count_15
		sum_16 = 0.5 * count_16
		sum_17 = 0.5 * count_17
		sum_18 = 0.5 * count_18
		sum_19 = 0.5 * count_19
		sum_20 = 0.5 * count_20
		sum_21 = 0.5 * count_21
		sum_22 = 0.5 * count_22
		sum_23 = 0.5 * count_23
		#This sums up the weights and total count of occurences in the paragraph.
		sum_total = sum_1 + sum_2 + sum_3 + sum_4 + sum_5 + sum_6 + sum_7 + sum_8 + sum_9 + sum_10 + sum_11 + sum_12 + sum_13 + sum_14 + sum_15 + sum_16 + sum_17 + sum_18 + sum_19 + sum_20 + sum_22 + sum_23
		count_total = count_1 + count_2 + count_3 + count_4 + count_5 + count_6 + count_7 + count_8 + count_9 + count_10 + count_11 + count_12 + count_13 + count_14 + count_15 + count_16 + count_17 + count_18 +  count_19 + count_20 + count_21 + count_22 + count_23
		#This filters out single-question paragraphs, which add noise to the summary and are usually redundant.
		if len(re.findall('\.', i)) < 1: #Single-question pars won't contain a period. Valuable single-sentence pars will contain a period. 
			average_score = 0
		#This filters out short paragraphs, which are likely to not contain any useful context. 
		#This doesn't apply when a speaker makes a correction.
		#Example of extracted text:
		#Senator Birmingham: The government has provided $2.1 million in the 2017-18 budget to support the authority. 
		#Funding arrangements for 2018-19 onwards will be subject to the usual budget processes.
		#Ms Evans: I might make a minor correction. There is a $1.456 million allocation. 
		#The briefing that we provided to the minister was incorrect.
		#Another example of extracted text:
		#Senator URQUHART: Again, this is to the minister, but if you want to flick it then I am sure you will. Can
		#you confirm that the allocation of money apportioned to the environment portfolio from the $1.1 billion in the
		#rollout of the National Landcare Programme moneys referred to in the budget will stay the same as previously?
		#Will it rise or will it fall between now and 2023?
		#Senator Birmingham: Just for the record, Senator Urquhart, it is $1.1 billion, not $1.1 million.
		elif len(i) <= 55: 
			if re.findall('incorrect', i) or re.findall('correction', i) or re.findall('mistake', i) or re.findall('should have said', i) or re.findall('I meant', i) or re.findall('for the record', i) or re.findall('For the record', i):
				average_score = 1 
			else:
				average_score = 0
		elif re.findall('incorrect', i) or re.findall('correction', i) or re.findall('mistake', i) or re.findall('should have said', i) or re.findall('I meant', i) or re.findall('for the record', i) or re.findall('For the record', i):
			average_score = 1 #Correcting a statement clould require an explaination of more than 55 chars. I'm working on 'sorry' in the context of a correction.
		elif sum_total == 0.0:
			average_score = 0 #Takes care of float division
		#This calculates the mean score of the paragraph.
		else: 
			average_score = sum_total/count_total
		#The below threshold ensures that only paragraphs with a high enough score will be included in the summary.
		#Paragraphs that contain high weigthed features will always make it through to the summary for one or more occurences (average score always above threshold).
		#Paragraphs that contain med to low weighted features will need a combination of weights to make it through to the summary.
		#0.6 is not too low where summary includes a lot of noise and is not too high where summary misses a lot of important info.
			if average_score > 0.6:
				summary.append(i)
	print title + '\n'
	print "\n\n".join(summary)
	
def function_2():
	count_vect = CountVectorizer()
	bow_matrix = count_vect.fit_transform(paragraphs)
	normalized_matrix = TfidfTransformer().fit_transform(bow_matrix)
	similarity_graph = normalized_matrix * normalized_matrix.T
	similarity_graph.toarray()
	nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
	scores = nx.pagerank(nx_graph)
	ranked = sorted(((scores[i],s) for i,s in enumerate(paragraphs)), reverse=True)
	ten_percent = int(round(10.00/100.00 * len(ranked)))
	ten_percent_high_scores = ranked[0:ten_percent]
	summary = [x[1] for x in ten_percent_high_scores] #Does not disturb the rank order, and overrides above summary.
	print title + '\n'
	print "\n\n".join(summary)

def main():
	if len(re.findall('\$', content)) < 2: #With more time, I can properly classify the input doc as being facts and figures type or discussion/opinion type.
		function_2()
	else:
		function_1()
		
if __name__ == "__main__": 
	main()

