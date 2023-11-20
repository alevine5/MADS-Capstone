# Zoonotic Forecast: A Data Science Approach to Predicting Viral Spillovers
![Summary image](https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20220615070525/ri/950/src/images/Article_Images/ImageForArticle_22674_16552911221244194.jpg)

## Summary
The emergence of zoonotic diseases—illnesses transmitted from animals to humans—poses a serious threat to global health security. Recent outbreaks underscore the urgent need for predictive analytics to preempt viral spillovers. This capstone project leverages data science to map the historical incidence of zoonotic viruses and forecasts future risks. By understanding patterns of past outbreaks and integrating demographic changes, our analysis aims to pinpoint potential hotspots before they flare into human epidemics, aiding policymakers and health organizations in crafting proactive defenses.

## Background Research
Zoonotic pathogens have repeatedly blindsided the human population, with the 21st century witnessing escalations in both frequency and impact. A [notable study](https://pubmed.ncbi.nlm.nih.gov/18288193/) by the Zoological Society of London synthesized the global trends of emerging zoonoses, highlighting the role of wildlife as a reservoir. [Another pivotal work](https://pubmed.ncbi.nlm.nih.gov/18288193/) by the UCLA Department of Epidemiology provided a framework for predicting the origins of future zoonotic viruses. Despite these advancements, the field still requires a nuanced risk assessment tool that accounts for evolving human-animal interfaces. Our project builds on these foundations, employing machine learning to assess and forecast zoonotic risk with unprecedented precision.

## Project Visualizations
Visualizations crafted for this project will serve as a window into the progression of zoonotic diseases across the timeline of human history. They will depict the frequency, distribution, and trajectory of past outbreaks, converting complex data into a compelling narrative. The intent is to clarify the role of factors such as demographic shifts and economic developments in disease emergence. We will first use interactive geospatial heat maps to show the risk of this type of emergence over the years, as well as pointing out the major outbreaks of this nature that have occurred in the past. Then, we will use line graphs with confidence intervals to show the trends of the risk scores of each country. Through these visualizations, we aim to show the factors affecting disease emergence, guiding observers in recognizing patterns that signify potential threats.

## Machine Learning Model Application
The heart of our predictive mechanism is a random forest regression model trained to scrutinize regions for zoonotic spill-over potential. This model assimilates diverse datasets, including demographic, economic, and historical epidemiological data to assign risk scores to each country. The outcomes will be translated into heat maps, highlighting areas with elevated risk. Then, we will use k-fold cross validation to derive reasonable confidence intervals for our risk score forecasts. We will demonstrate these predicted risk scores via line graphs. This innovative approach is designed not just to forecast future outbreaks but to empower targeted surveillance and pre-emptive interventions, potentially saving millions of lives by alerting to the rumble of the next pandemic before it roars.

# How to Contribute

### Cloning the Repository
To start working with the project code, you need to clone the repository to your local machine. Use the following command:
```
git clone https://github.com/alevine5/MADS-Capstone/
```

### Creating a branch
Branches allow you to work on new features or fixes without affecting the main codebase. To create and switch to a new branch:
```
git checkout -b feature-branch-name
```
Try to use a name that reflects the purpose of the changes you're making.

### Making Changes and Committing
After making changes to your branch, you need to commit them with a clear message:
```
git add .
git commit -m "A descriptive message about the changes"
```
Instead of period you can also use the file name to stage just one file instead of everything.

### Pushing Commits to GitHub
Once you've committed your changes, push the branch to GitHub:
```
git push origin feature-branch-name
```

### Creating a Pull Request (PR)
To open your changes to review, or to merge your changes into the main codebase, create a PR:
1. Go to the repository on GitHub.
2. Click on 'Pull Requests' and then the 'New Pull Request' button.
3. Select your branch and provide a summary of the changes. Then create the pull request.

## Github Project Management

### Issues
If you encounter a bug or want to suggest a feature, open an issue:

1. Navigate to the 'Issues' tab in the GitHub repository.
2. Click on 'New Issue', provide a title and detailed description.
3. Assign labels to categorize the issue (e.g., bug, enhancement).

### Categorizing Issues

**Assigning the Issue**

Assign issues to specific individuals when you believe they are best suited to tackle the problem or when they are responsible for that aspect of the project:

1. On the issue page, click on 'Assignees'.
2. Choose a collaborator's name to assign the issue.

**Milestones**

Use milestones to group issues and pull requests into manageable phases or iterations of work:

1. In the 'Issues' or 'Pull Requests' tab, click on the 'Milestone' button.
2. Select an existing milestone or create a new one to associate with the issue or PR.
3. You can set a deadline to a specific milestone as a reminder

**Projects**

We organize our workflow using GitHub Projects to get a high-level overview of progress. For this project we are using a typical project management board with categories "Blocked", "TODO", "In Progress" and "Done":

1. In the GitHub repository, navigate to 'Projects' and select or create a new project.
2. Within the project, you can drag and drop issues to recategorize them.
3. Once an issue is done, click on the issue and click "close issue" to both close the issue and move to "Done"
4. If you have a PR that closes an issue, put "This closes [link to issue]" so that when the PR is merged, it will automatically both close and categorize the issue as closed/done.

**Best Practices**

- Always pull the latest changes from the main branch before starting new work.
- Keep commits small and focused; one feature or fix per commit.
- Try to keep one PR per feature/issue. This makes them easier to review.
- Typically we want to request review on a PR from the person that created the issue, just to make sure it addresses the ask.
- Write meaningful commit messages and PR descriptions.
- Respect the code style and conventions established in the project.
- Engage in peer code reviews constructively and respectfully.

## Contact Us
If you have any questions, reach out to us at:

- [Samuel Buxton](sambux@umich.edu)
- [Alex Levine](ajlev@umich.edu)


![University of Michigan Logo](https://brand.umich.edu/assets/brand/style-guide/logo-guidelines/U-M_Logo-Horizontal-Hex.png)

