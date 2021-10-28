# EDA_with_Python

A continuación una copia del manual de usuario y el libro de codigos compartido por el "Mass Mobilization Data Project".

Mass Mobilization Data

Data on protest actions at the level of the protest has been relatively sparse; this users manual provides the description for data on protests against governments, what protesters demand, and how governments respond. The data cover the globe, 162 countries, 1990-2014.
The unit of observation is the protest-country-year, where protests are recorded individually within each country and year. The data file consists of the following variables:

1) Unique case identifier
2) Country name
3) Country code (Polity code)
4) Year
5) Region
6) Protest
7) Protest number in year
8) Start day
9) Start month
10) Start year
11) End day
12) End month
13) End year
14) Protester violence
15) Protest location
16) Number of participants
17) Protester identity
18) Protester demands [4 variables denoting demands]
19) State responses [7 variables denoting state responses]
23) Sources
25) Notes
26) Categorical indicator of participation [added part way through coding, not available for all cases]

Method of searching:

The aim of the project is to identify any protest event where the protest targets the government, and where it involves at least 50 people. Coders search Lexis-Nexis, “All News,” using “advanced options” which permit selection of “major world publications,” entry of date ranges, country name, and search terms. Each search period initially ranges from January 1 – December 31 of each year, for each country. The search period is shortened where the number of search results for the year exceeds LN’s maximum.

The search is in Lexis-Nexis for four key words:
Protest 
Demonstration 
Riot
Mass Mobilization

Every search is for these four terms joined by a Boolean “OR” term – so search for protests OR demonstrations . . . etc.

The search is restricted to newspaper sources – it proceeds as follows.

First, search for the four terms above in a country, over a year in four primary sources:

New York Times Washington Post Christian Science Monitor Times of London

In MENA, consider these four sources plus the Jerusalem Post.

If these sources return more than 100 articles, then proceed in searching the articles for evidence of codeable protest events. If these four sources do not return at least 100 articles, then expand the search to include regional and other sources. Proceed with coding protest events. Note that sometimes even this more source-inclusive search will not return 100 articles – in this case, add wire-reports to the search – then code appropriate protest events regardless of total articles returned. These procedures and additional mechanical instructions for searching are recorded in the document “Mass Mobilization Coding Procedure.”

Variable Descriptions:

Country Name: Polity’s country name.
Country Code: three-digit Polity Project country code. 
Year: 1990- 2014
Region: Regions correspond to Polity code breaks:
1. South America – country codes 100-165
2. Central America – country codes 40-95
3. North America – country codes 20-70
4. Europe – country codes 200-390
5. Asia – country codes 700-910
6. MENA – country codes 600-698
7. Africa – country codes 402-590
Protest: is a dichotomous coding for whether or not there was a protest action in a particular period
The project defines a protest as a gathering of 50 or more people to make a demand of the government. A protest action must be targeted at the state or state policy. The project does not code protests in one country that are targeted at the policies of another country and in that sense, it captures only “home grown” protest activities targeted at state policies.

We are interested in mobilization of anti-state protest, not necessarily community disputes between various groups, and therefore we do not code inter-communal demonstrations. For example, Christians and Muslims in a specific community might display discord of some sort by means of protesting or demonstrating against their communal rival. Even if those actions require police involvement we do not code it as an anti-state protest. Protests that involve an industrial enterprise that is affected by state policy such as labor rights or safety, does represent a codeable activity only if the people take to the streets to
demand better conditions, wages, safety, and the outcome is a function of state level policy decisions. A union action targeted specifically at conditions linked to a specific company and are part of labor negotiations do not constitute a protest, unless or until the labor action becomes a public event (by, say, marching in the streets or demanding action on the part of the government).

We do not code data on rebel attacks or other types of armed resistance to the state. So a “group of rebels” that attacks a police or army outpost is not of interest to us. But if a group identified as a rebel organization engages in protest, this would be a codeable event. We do not code political rallies. Although armed rebel action and political rallies reflect the expression of political opposition, neither captures the type of anti-state protest of interest to this project. A political rally is one in which two or more political parties demonstrate in support of their political positions and are associated with upcoming elections. In this sense they might be thought of as the quintessential pro-state action. Armed rebel action is certainly anti-state in character but it has already crossed a threshold where it no longer reflects an expression of a demand to be redressed but rather a means of obtaining some demand by force of arms.

Start and End Dates: We record the dates marking the beginning and ending of the protest action. In the case of a one-day protest, start and end dates are the same. The beginning date is generally the easier of the two, marking the first time records show that a group of 50 or more participants organized together to press a demand in a public forum. The end date reflects when reporting describes either the physical end to the protest or the last date that there is a report on the protest activity. In theory a protest action could simply go below the radar of reporting but in practice the end is usually noted just as the beginning is. For long protest it was necessary to follow the reporting over weeks and often months to make sure that the end date reflected the end of the protest action rather than a lull in the reporting.

Protester Violence: we record whether protesters engaged in violence against the state. This is a dichotomous coding that does not take into account any aspect of the type of violence used. The violence could include anything from riotous behavior that destroys property to shooting at the police or military.

Locations: We record the location of the protest as specifically as possible, though specificity varies with reporting. Some reports provide neighborhoods, others just the city, others only the province. If protests took place in multiple locations, each is listed. When a protest is national in organization we record it as such. The difference between a series of local protests and one national protest turned on whether it appeared to be organized nationally rather than some number of individual protests on the same day. To make this distinction we tried to rely on the demands and the group identity of the protesters.

Number of Participants: Estimates of the number of participants at a protest event are notoriously vague and variable. Two different sources might report wildly divergent numbers. We relied on the lower of any estimate at one point in time, but if a protest extended beyond one day and the number of protesters grew with time, we would rely on the maximum number of participants at any point in the protest. If a report described the arrest of, say, 40 protesters but not the total number of protesters involved, the coder made a decision based on the report as to whether or not this constituted a codeable event. This required inferring whether the population of arrested persons was less than the population of protesters.

Categorical Indicator of Participation: Part way through the coding, we added a categorical indicator – this is in addition to the raw number above, but an effort to standardize our coding. Categories are:
• 50-99
• 100-999
• 1000-1999 • 2000-4999
• 5000-10000 • >10000

Protest Group Identity: This variable records the name or identity of the group involved in or organizing the protest. Where possible, it records the hierarchy and identity of the protesters.

Protester Demands: We identify seven categories of protester demands that describe the types of issues that motivate protest behavior. Any protest event can have multiple demands. We code up to four protester demands. The seven categories are:
1. Labor or wage dispute: Given the restrictions mentioned above, this category captures demands against state policy that influence labor conditions or wage rates. In many countries the state sets labor policy (safety, working hours, etc) or minimum wages. Further, many industries are state owned or state controlled and as such the state exercises control over wage rates at a specific industry. A wage strike in a private industry that does not involve state policy is not coded as a protest.
2. Land tenure or farm issues: Access to or restrictions imposed on the use of land are coded in this category. A state that requisitions land from, say, farmers for a dam project might generate a protest over land use. If state policy affects the use of certain land and that policy generates a protest action demanding redress to that policy, it is coded here.
3. Police brutality or arbitrary actions: This category captures demands against the treatment of citizens by the authorities. The beating or jailing of people for seemingly arbitrary reasons, the brutality by police or other authority figures against a group or individual would be recorded under this demand.
4. Political behavior/processes: This is the broadest category and captures aspects of the political process that determines who rules and how, who can participate in elections or decisions, choices made by leaders that influence a range of political outcomes from domestic subsidies to foreign policy. The general category of demanding “reform” would be captured by political behavior or processes, as would demands for democratic transitions.
5. Price increases or tax policy: This category accounts for demands over subsidies, tax increases or levies, the cost of food, utilities or other such necessities.
6. Removal of corrupt or reviled political person: if the protest is about official corruption or the corruption of a particular individual, this category would capture this demand. This category can be distinct from the conditions where protesters demand political reforms because of corruption, such as would be capture under category #2. Here we are primarily looking for systematic corruption that generates a demand for the removal of an individual or small group within the government.
7. Social restrictions: Social restrictions capture the imposition of constraints on interactions among or between groups, the banning of various social behavior (head scarves, lotteries, etc), or the banning of the rights of a particular group.

State Response: We identify seven types of actions (or inaction) the state might take in response to protests. The state often responds in multiple ways; we code up to seven government responses to a protest event. Killing is the most extreme – it is important to note government intent to kill is not part of the coding process; we code whether or not government kills protesters, not whether they mean to. In practice, shootings, killings, and beatings might be thought of as an aggregated category of deadly or potentially deadly force.
1. Accommodation of demands, indicated by agreeing, negotiating, etc.: this is indicated by reports that the authorities met with protest leadership; that the demand was met or that the authorities agreed to take the protester demands up in a formal meeting.
2. Arrests
3. Beatings
4. Crowd dispersal mechanisms: any attempt to move the protesters from their location and break up the protest, short of means that are more violent and captured in the categories above. Examples might include the use of tear gas, issuing warnings, moving troops into position and pushing protesters off their positions.
5. Ignore: ignoring a protest action can be the result of two different processes. One is that the news outlets simply ignore the response by the state; the other is that the state does not react to the protest action. In the process of coding it was difficult or impossible to disentangle to two explanations for no reporting on the state actions. Intuition suggests that much of the lack of response reflects a state strategy rather than the inability of a reporter to describe how the state responded. For instance it strains reasoning for a reporter to describe the demand, the group and protester violence without mentioning how the state responded, unless the state simply let the protesters have their say. You can pick up some trace of this in multiday protest where there might not be a recorded response on day one but as the protest endures the state begins to respond and reporters begin to report that response.
6. Killings
7. Shootings

Sources, notes: Sources provide an identification of the article(s) used to code the particular protest; notes describe any information that might have informed the coding decision. Notes also comment on the facts of the protest events, often quoting from main sources.
