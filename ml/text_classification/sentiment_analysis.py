import spacy

nlp=spacy.load('en_core_web_lg')

print(nlp(u'lion').vector)

tokens=nlp(u'lion cat pet')




#so by this we can say that it is having the simmilar meaning here so searching and all is very gets simmilar here...
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text,token1.similarity(token2))
        

print(nlp.vocab.vectors)

print(nlp.vocab.vectors.shape)


tokens=nlp(u"dog cat nargle")

for token in tokens:
    print(token.text, token.has_vector,token.vector_norm,token.is_now)

#Excellent question. Let’s break it down with an analogy and clear logic:

# 🎯 Your Question:
# If normalization reduces the vector’s values, how does it still help find the direction?

# 🔭 Think of a vector as an arrow:
# The arrow’s direction points somewhere in space.

# The length (norm) is how far it stretches.

# When you normalize, you're just:

# ✂️ Shrinking the arrow’s length to 1
# 🧭 But NOT changing which way it points

# 📐 Geometry view:
# Let’s say we have:

# java
# Copy code
# Vector A = [3, 4]
# Its direction is the ratio between its values:

# css
# Copy code
# 3 (x-direction), 4 (y-direction)
# Even if we normalize:

# ini
# Copy code
# A_normalized = [0.6, 0.8]
# The proportion is the same:

# Copy code
# 0.6 / 0.8 ≈ 3 / 4
# So, it still points in the same direction — just with shorter length.

# 🧠 Why is this helpful?
# When we use cosine similarity, we only care about direction, not size.

# Example:

# Let’s compare:

# "king" → [3, 4]

# "queen" → [6, 8]

# Their cosine similarity = 1.0 (perfect match)

# Even though one vector is twice as long, their direction is the same.

# So normalization removes the size and lets us focus only on meaning (direction).

# ✍️ Summary:
# Normalization reduces the size of a vector but keeps its direction, so we can fairly compare how similar two word meanings are, without size bias.


from spacy import spatial

cosine_similarity=lambda vec1,vec2: 1 - spatial.distance.cosine(vec1,vec2)


king=nlp.vocab['king'].vector
man=nlp.vocab['man'].vector
woman=nlp.vocab['woman'].vector

#king-man+woman--->NEW_VECTOR similar Queen , princess, highness

new_vector=king-man+woman

computed_similarities=[ ]

for word in nlp.vocab:
    if word.had_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity=cosine_similarity(new_vector,word.vector)
                computed_similarities.append((word,similarity))
                
computed_similarities=sorted(computed_similarities,key=lambda item:-item[1]) 
          
#so by this way we can find the similarities betwene the vector here and how it is closed to each other here and how it is excatally working here...add()                        
print([t[0].text for t in computed_similarities[:10]]) 
           