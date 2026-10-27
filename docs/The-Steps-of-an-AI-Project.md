# The Steps of an AI Project


A team built a model that predicts whether a customer will cancel their subscription. Their notes are in the wrong order:

a.Trained a model on 80 percent of the customers

b.Found that 300 customers had no start date

b.Decided that the question was "which customers cancel within three months?"

d.Measured the model on the other 20 percent

e.Fetched two years of customer data from the customer system

f.Made figures of how the cancellations were spread over the months

g.Made a script that the marketing team can run once a week

h.Saw that the model was much worse for new customers, went back and added a column

Answer three questions:

1.Put the notes in the order of the seven steps in The Workflow of an AI Project.

2.Which step did the team go back to, and why?

3.In note h, the team saw that the model was worse for new customers. What must they have measured to see that? Think about what one number for all customers together would have shown.

# 1 The correct order


## Following the typical AI project workflow:


# 1.Define the problem (C)

Decided that the question was "which customers cancel within three months?" (Note 3)

# 2. Collect data (e)

Fetched two years of customer data from the customer system (Note 5)

# 3. Prepare and clean the data (b)

Found that 300 customers had no start date (Note 2)

# 4.Explore and understand the data (f)

Made figures of how the cancellations were spread over the months (Note 6)

# 5.Train the model (a)

Trained a model on 80 percent of the customers (Note 1)

# 6.Evaluate and improve the model (h)

Measured the model on the other 20 percent (Note 4)
Saw that the model was much worse for new customers, went back and added a column (Note 8)

# 7. Deploy the model (G)

Made a script that the marketing team can run once a week (Note 7)


## 2. Which step did the team go back to, and why?

The team went back to data preparation / feature engineering (Step 3).

They discovered that the model performed much worse for new customers. To improve the model, they added a new column (feature) that provided additional information the model could learn from. After adding the column, they would need to train and evaluate the model again.

## 3. What must they have measured to see that the model was worse for new customers?

They must have measured the model's performance separately for different customer groups, such as:

New customers
Existing customers

If they had looked at only one overall accuracy number for all customers combined, the poorer performance on new customers might have been hidden by the better performance on existing customers.