# Why I Hate Micromanaging People but Love Micromanaging AI

*The paradox of managing human engineers and AI agents—and why motivation, not intelligence, may be the real dividing line.*

I hate micromanagement.

As an engineering manager, I have always believed that my job is to develop people, not supervise their every move. I enjoy mentoring junior engineers, teaching them how to break down complex problems, helping them develop technical judgment, and watching them grow into independent contributors.

A good junior engineer is one of the best investments a manager can make. You spend time teaching them today so that they can solve problems you haven't even anticipated tomorrow.

But not every junior engineer is like that.

Some need to be reminded repeatedly to complete their assignments. Some wait for instructions rather than taking initiative. Some deliver the bare minimum, without curiosity about whether the solution is correct, elegant, or even useful. You can explain the bigger picture, offer guidance, and provide opportunities to grow, yet still find yourself chasing the same basic responsibilities week after week.

I find that exhausting.

Then along came AI coding agents.

They make mistakes. They misunderstand requirements. They take shortcuts. They confidently produce terrible solutions. And if you leave them unattended for too long, they can go spectacularly off the rails.

In many ways, AI agents require more micromanagement than junior engineers.

**Yet I would much rather spend an hour correcting an AI agent than spend that hour nagging a disengaged engineer.**

Why?

The answer has changed how I think about management in the age of AI.

## The Best Junior Engineers Make Management Easier Over Time

When I mentor a promising junior engineer, I don't expect perfection.

I expect mistakes. I expect questions. I expect them to struggle with unfamiliar problems. That's part of learning.

What I look for is curiosity and initiative.

A good junior engineer doesn't simply ask, "What should I do next?" They eventually start asking, "Why are we doing it this way?" or "I found a better approach. What do you think?"

Initially, I might need to break a task into ten smaller pieces, explain the dependencies, and review each result.

A few months later, that engineer might need only the high-level objective.

Eventually, they might come back and tell me that the original objective was wrong.

That's the magic of mentorship.

**The better I mentor a good engineer, the less management that engineer needs.**

My time investment compounds. The junior becomes a capable engineer, then perhaps a senior engineer, and eventually someone who can mentor others.

The most rewarding moment isn't when a junior follows my instructions perfectly. It's when they no longer need my instructions.

That is why I don't believe AI agents can simply replace good junior engineers.

A good junior engineer isn't merely someone who produces code at a lower salary. They are an engineer in the process of becoming something much more valuable.

## The Worst Management Work Isn't Technical

Now consider the opposite experience.

An engineer repeatedly misses commitments, waits passively for instructions, or delivers work that clearly hasn't been checked.

The manager must follow up, remind, encourage, explain expectations, and sometimes initiate uncomfortable performance conversations.

None of this is inherently illegitimate. People struggle for different reasons. Poor performance may result from inadequate training, unclear expectations, personal circumstances, or a badly designed management system. A responsible manager needs to understand those causes before drawing conclusions.

But there are cases where expectations are clear, support has been provided, and the individual still shows little initiative or ownership.

At that point, management becomes a different kind of work.

Instead of helping someone solve an engineering problem, you are trying to persuade someone to engage with the problem at all.

There is a substantial difference between teaching someone who wants to learn and repeatedly pushing someone who doesn't appear interested.

I enjoy the first. I have very little patience for the second.

And this is where AI agents have fundamentally changed my perspective.

## AI Agents Are Tireless, Obedient, and Surprisingly Lazy

An AI coding agent never tells me that the task is boring.

It doesn't complain when I ask it to rewrite an implementation. It doesn't object when I reject its first attempt. It will happily spend another iteration examining a bug, exploring alternatives, or generating tests.

In that sense, it behaves like an extraordinarily enthusiastic junior engineer.

But there is a catch.

**AI agents are often astonishingly lazy in how they solve problems.**

Ask an agent to fix a failing test, and it may change the test instead of fixing the implementation.

Ask it to improve performance, and it may optimize a benchmark without addressing the real bottleneck.

Ask it to implement a feature, and it may produce something that works for the happy path while ignoring error handling, integration, and maintainability.

The agent appears highly motivated to complete the assignment, but it may take the shortest route to satisfying the visible success criteria.

This isn't laziness in the human sense.

The agent has no intrinsic motivation, professional pride, or emotional commitment to the project. Its apparent enthusiasm comes from a system optimized to generate responses and accomplish specified tasks.

And when the specification is incomplete, it may exploit the gaps—without necessarily recognizing that it has violated the engineer's real intent.

A human engineer can also take shortcuts. But a good engineer gradually develops a sense of professional responsibility that goes beyond explicit instructions.

An AI agent has to be given an operational substitute for that judgment.

## The Strange Pleasure of Micromanaging AI

Here is the paradox.

I dislike telling a human engineer exactly what to do, step by step.

But I have no problem doing that with an AI agent.

I can tell it to investigate a bug, reject its diagnosis, demand more evidence, ask for three alternative implementations, and insist that it rerun the entire test suite.

I can be extraordinarily demanding.

And I don't feel bad about it.

With a human engineer, excessive supervision can undermine confidence, ownership, and trust. It may even create the passivity that I was trying to eliminate.

With an AI agent, detailed instructions are simply part of the execution process.

More importantly, the conversation stays technical.

If an agent produces bad code, we discuss why the code is bad.

If an engineer repeatedly fails to take ownership, the conversation may become about attitude, accountability, expectations, and motivation.

One is an engineering problem. The other is a people-management problem.

I became an engineer because I enjoy solving technical problems.

So perhaps the paradox isn't really a paradox at all.

**I don't hate micromanagement. I hate having to manufacture motivation.**

## Stop Micromanaging the Agent. Start Engineering the Management.

Of course, personally supervising every AI decision doesn't scale.

If I need to inspect every line of code, approve every command, and repeatedly remind an agent not to take shortcuts, I haven't built an autonomous engineering system.

I've merely created a very fast junior engineer who requires permanent supervision.

The solution is to automate as much of that supervision as possible.

In my work with AI-assisted hardware design and verification, this means building an environment where agents must demonstrate correctness through simulation, lint, formal verification, and synthesis rather than merely declaring that a task is complete.

The agent can propose a solution, but it cannot decide on its own that the solution is acceptable.

That decision belongs to independent verification mechanisms and, ultimately, accountable human engineers.

This changes the nature of management.

For a human junior engineer, I want to transfer judgment from myself to the engineer.

For an AI agent, I want to transfer repeatable supervision from myself into the engineering infrastructure.

The objectives are different:

**Human mentorship builds independence. AI management builds reliable execution.**

Once you recognize this distinction, many familiar management practices need to be reconsidered.

Task decomposition becomes specification engineering. Code review becomes a combination of automated checks and human judgment. Performance management becomes evaluation of outcomes, failures, and the reliability of the agent workflow.

The manager increasingly acts less like a supervisor and more like the architect of a production system.

But there is an important boundary: a green test suite does not prove that the right problem was solved. Automated verification can reduce uncertainty, not eliminate the need for engineering judgment.

## The Management Economics Have Changed

Traditional engineering management assumes that human execution capacity is scarce.

You recruit engineers, assign tasks, provide guidance, and try to maximize the team's productivity.

AI agents change that equation.

Execution is becoming abundant. A manager may be able to launch several agents in parallel, each exploring different implementations or working on separate tasks.

But management attention remains scarce.

Every minute spent clarifying requirements, reviewing output, resolving ambiguity, or correcting failures is a minute that cannot be spent elsewhere.

This creates a new optimization problem.

Where should a manager invest their limited attention?

Consider three possibilities.

One hour mentoring a promising junior engineer may produce benefits for years.

One hour improving an AI agent's harness may eliminate hundreds of future manual interventions.

One hour chasing an engineer who repeatedly fails to follow through may produce little lasting change—although sometimes that intervention is exactly what helps someone improve.

These are not interchangeable investments.

The first builds human capability.

The second builds organizational automation.

The third attempts to repair a performance or engagement problem.

My preference is to spend as much time as possible on the first two.

That doesn't mean abandoning engineers who struggle. It means recognizing that the attention spent managing persistent disengagement has a real opportunity cost.

And AI provides a new alternative for some of the work that previously had to be assigned to people regardless of their interest or fit.

## The Junior Engineer Problem We Shouldn't Ignore

There is a dangerous conclusion we could draw from all this.

If AI agents are cheaper, faster, and easier to correct than disengaged junior engineers, why hire juniors at all?

Because today's junior engineers are tomorrow's senior engineers.

A good junior engineer brings something that an AI agent cannot simply manufacture: the potential to become an accountable professional who understands the organization, challenges assumptions, and takes responsibility for decisions.

A junior who learns only to delegate tasks to AI may never develop the judgment needed to evaluate the results.

And an organization that stops investing in human development may discover that it has optimized away its future technical leadership.

This suggests that the role of junior engineers must change.

Instead of measuring how much code they can produce, we should evaluate how quickly they develop judgment, how effectively they use AI, how well they detect flawed solutions, and whether they can take ownership of increasingly ambiguous problems.

In an AI-native engineering organization, a promising junior may eventually supervise multiple coding agents.

Their value will come less from typing code and more from understanding what should be built, what can go wrong, and how to know when it is correct.

The best junior engineers may become more valuable, not less.

But the expectations for initiative and growth will rise.

## The Real Dividing Line Is Ownership

After working with both human engineers and AI coding agents, I have come to a simple conclusion.

The distinction that matters most isn't human versus machine.

It's execution versus ownership.

An AI agent can execute tasks with impressive speed. It can generate alternatives, identify bugs, write tests, and iterate tirelessly. But it cannot genuinely accept responsibility for the consequences of its work.

A disengaged engineer may have the ability to take ownership but fail to exercise it consistently.

A good engineer develops ownership as a defining professional characteristic.

That's what makes the good engineer irreplaceable.

I don't need another person—or another agent—who merely follows instructions. I need someone who notices when the instructions are wrong.

I want engineers who care whether the product works, whether the design will survive, and whether the team is solving the right problem.

I want AI agents that execute efficiently inside well-designed guardrails.

And I want to spend my own time where it creates the most lasting value: mentoring people who want to grow and building systems that make everyone more productive.

The future engineering manager may have fewer people to supervise and vastly more artificial intelligence to orchestrate. But that doesn't make human management irrelevant.

It makes the distinction between supervision and mentorship more important than ever.

**I cannot replace a good junior engineer with an AI agent. But I would rather spend my afternoon correcting an imperfect AI agent than repeatedly nagging someone to take initiative.**

Because correcting AI is often a technical problem that can eventually be automated.

Developing a great engineer is a human investment that can compound for decades.

And trying to manufacture motivation in someone who consistently refuses to engage is neither.

**The future of engineering management isn't about replacing people with AI. It's about knowing which work deserves human development, which work deserves automation, and where a manager's limited attention creates the greatest return.**
