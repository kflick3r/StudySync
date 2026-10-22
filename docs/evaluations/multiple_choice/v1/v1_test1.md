# StudySync: Multiple Choice V1 — Test 1 Generated Questions

**Topic:** Logistic Regression  
**Questions Generated:** 10  
**Source:** Logistic Regression course notes  
**Prompt Version:** V1

---

### Question 1

**What type of response does logistic regression predict?**

A. A textual sequence  
B. A hidden Markov state  
C. A categorical response  
D. A continuous numerical response

**Correct Answer:** C. A categorical response

**Explanation:** Logistic regression is a classification method used to predict a categorical response.

---

### Question 2

**What range of values can the estimated probability p(X) take in logistic regression?**

A. Any real number from negative infinity to positive infinity  
B. Between -1 and 1  
C. Only strictly between 0 and 1 exclusive  
D. Between 0 and 1 inclusive

**Correct Answer:** D. Between 0 and 1 inclusive

**Explanation:** Because p(X) is a probability, it satisfies 0 ≤ p(X) ≤ 1.

---

### Question 3

**How does lowering the classification threshold from 0.5 to 0.1 affect a credit card classifier?**

A. It changes the coefficients beta0 and beta1 automatically.  
B. It restricts the model to only predict the negative class.  
C. It turns the logistic function into a linear regression model.  
D. It makes the classifier more willing to predict the positive class.

**Correct Answer:** D. It makes the classifier more willing to predict the positive class.

**Explanation:** Lowering the threshold (for example to p(X) > 0.1) makes the classifier more willing to predict the positive class.

---

### Question 4

**For a single predictor with the standard threshold of 0.5, where does the decision boundary occur?**

A. Where p(X) = 0  
B. Where p(X) = 0.1  
C. Where p(X) = 0.5  
D. Where p(X) = 1

**Correct Answer:** C. Where p(X) = 0.5

**Explanation:** For the standard threshold of 0.5, the decision boundary occurs where p(X) = 0.5.

---

### Question 5

**Why is linear regression poorly suited for binary classification compared to logistic regression?**

A. Linear regression only works with a classification threshold of 0.1.  
B. Linear regression cannot calculate coefficients from training data.  
C. Linear regression requires categorical predictors.  
D. Linear regression can produce predictions outside the valid probability range.

**Correct Answer:** D. Linear regression can produce predictions outside the valid probability range.

**Explanation:** Linear regression is poorly suited for binary classification because it can produce predictions outside the valid probability range, whereas logistic regression produces values bounded between 0 and 1.

---

### Question 6

**In the logit form of the logistic function, what does the sigmoid function do to the logit z?**

A. Converts it into a continuous unbounded score  
B. Multiplies it by the bias term  
C. Converts it into a probability  
D. Extracts the feature weights

**Correct Answer:** C. Converts it into a probability

**Explanation:** The sigmoid function converts the logit into a probability.

---

### Question 7

**In the beta notation of the logistic model, what does the intercept term beta0 correspond to in the logit form?**

A. The predicted probability p(X)  
B. The input feature x  
C. The bias or intercept b  
D. The feature weight w1

**Correct Answer:** C. The bias or intercept b

**Explanation:** In the logit form, b corresponds to the intercept beta0.

---

### Question 8

**What does a positive weight assigned to a feature indicate in logistic regression?**

A. That the feature has no influence on the prediction  
B. Evidence toward the positive class  
C. That the feature value is greater than 1  
D. Evidence toward the negative class

**Correct Answer:** B. Evidence toward the positive class

**Explanation:** A positive weight provides evidence toward the positive class.

---

### Question 9

**How does a larger absolute weight affect a feature's role in the model's prediction?**

A. It forces the feature weight to become negative.  
B. It gives the feature a weaker influence on the prediction.  
C. It gives the feature a stronger influence on the prediction.  
D. It turns the feature into a bias term.

**Correct Answer:** C. It gives the feature a stronger influence on the prediction.

**Explanation:** A larger absolute weight represents a stronger influence on the prediction.

---

### Question 10

**If P(y=1 | x) is computed by the model, how is P(y=0 | x) determined for a binary classification problem?**

A. 1 - P(y=1 | x)  
B. 1 / P(y=1 | x)  
C. Sigma(w * x - b)  
D. P(y=1 | x) - 1

**Correct Answer:** A. 1 - P(y=1 | x)

**Explanation:** P(y=0 | x) is calculated as 1 - P(y=1 | x).