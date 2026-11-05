"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            """In Freire’s “The Banking Concept of Education” he describes this idea of education being robotic, stuck in traditions and oppressive. In this system one participant, the teacher,deposits information and the other participant, the student, is a container for that information. This style of education puts the teacher as the ultimate authority and in a position of power. Students are seen as objects, ignorant and unable to learn and grow by themselves. Freire exemplifies this by the quote, “The teacher presents himself to his students as their necessary opposite; by considering their ignorance absolute, he justifies his own existence.” This description of the banking style of education utilizes Pathos to emotionally grab the reader into feeling a certain way about this education style.This style of education not only oppresses the students this way but also suppresses the increase of knowledge in society. Freire states, “Knowledge emerges only through invention and re-invention, through the restless, impatient, continuing, hopeful, inquiry human beings pursue in the world, with the world, and each other.” This logical, Logos, appeal relates how the banking style of education doesn’t allow for knowledge to grow because it requires its subjects to be static, unfeeling objects that are unequipped to tackle a world that would require them to seek out newness and strive to invent. The banking style of education sounds dreadful the way Freire describes it in his paper. At its basic root of the style is set up as a system that can be autonomous and has no need for major changes, outside basic maintenance. The reason for this is because it creates its own future. Students who belong to the banking concept go into the world and follow along and never grow or create anything. Then they have children of their own, begin to raise them in the way they were raised and taught, and then their children go into the same style of education. The cycle continues.""",
            """Problem posing education, on the other hand, promotes the opposite. It allows the student to become more than an object by creating a relationship between the teacher and the student that is not reliant on authority or absolute knowledge. Not only are students allowed to ask questions or speak opinions, but they are also encouraged! Freire describes this style of education as consisting “of cognition, not transferals of information,” in other words information is being given to be understoodnot just heard and stored for a later test. To establish some credibility, Ethos, Freire gives an example of a student-teacher interaction in a group in Chile that was discussing the anthropological concept of culture. A student in the middle of the discussion stated, “‘Now I see that without man there is no world.”’ This thought not only showed some understanding of the material being discussed, but also showed the difference between the two styles of education. The example does further with, “When the educator responded: ‘Let’s say, for the sake of argument, that all men on the earth were to die, but that the earth itself remained, together with trees, birds, animals, rivers, seas, the stars… wouldn’t all this be a world?’ ‘Oh, no,’ the peasant replied emphatically. ‘There would be no one to say: ‘This is a world.’” The student felt comfortable making a statement and the teacher, instead of shutting down the conversation and maybe even getting angry because the student was going off topic, posed a question that would encourage more thinking. Even though you could tell the teacher, by how they posed the question, was attempting to get a specific response, the student happily continued with what they were thinking.This is just a little bit of the positives when it comes to the problem posing style of education. Problem posing also allows students to realize their humanity and their place in the world. Shows and teaches them that they matter and encourages them to seek out more knowledge. Seeking out new and exciting things is paramount to innovation and to the overall survival of the world. Problem posing creates students that go into the world, ready to make change and affect the status quo. This creates a far more sustainable world then the one that runs on automatic.""",
            """A problem posing classroom would be a classroom when you walk into it, majority of the students are attentive to the subject. The classrooms would be generally louder than the banking style types of classrooms because there are conversations, dialogues, as opposed to monologues. Small group activities or large class group activities would probably be abundant in these classrooms resulting in a great sharing of ideas and thoughts which in turn encourage others to have more ideas and thoughts. You’d probably encounter many eager students who are confident in their ability to share and communicate with the teacher and the class. Communication would be prevalent, almost like a tennis match where the teacher may pose a question or statement and then a student (or students) might pose an answer or counter statement. This may encourage others to either agree or disagree with the answer or statement and the teacher would allow the discussion to continue. At this point the teacher almost becomes a facilitator of knowledge. Out of all this, students would probably be taking away joy and possibly hunger for more education and knowledge. They might even find new passions that they never knew or thought they may have. They would have a desire to learn more about whatever they find themselves passionate about. Students would take away how to act and help the world that they would be entering.""",
            """Overall,problem posing is a much better style of education. It’s very apparent in the paper that Freire dislikes the banking style concept. As it’s described, it is very hard to disagree with him. As he states in his paper the banking style is “Based on a mechanistic, static, naturalistic, spatialized view of consciousness, it transforms students into receiving objects.”The problem posing style offers way more opportunities for growth and innovation and encourages learning. Dialogue is encouraged through encouraging and expecting questions. Banking really encourages rote memorization without understanding and avoids questions especially if it challenges the ones in authority or power. While there are times when listening and following directions are necessary for overall success, the way it’s presented in the banking style teaches following authority simply because they are in authority.""",
            """With the much large resistance values (1 MΩ, 470 kΩ, 100 kΩ) there was little to no current being pulled, resulting in almost no voltage drop. With a low resistance of only 50 Ω, there was a noticeable voltage drop measured, resulting in lower voltage being measured than what the calculations tell us to expect.""",
            """The datasheet specifies a standard 50-ohm output impedance. However, due to the large resistance of the 1 MΩ and 470 kΩ resistors, the effect of the 50 Ω resistance on the voltage drop was very minimal, affecting no real change that could reliably be measured with the DMM. The result was that the math became distorted, resulting in inaccurate numbers returned.""",
            """Specifically for the 1 MΩ resistance, the voltage drop was 0 which resulted in an apparent resistance of 0 Ω. For the 470 kΩ, the effect of the internal resistance was better measured, however it was still small that the 470 kΩ still overshadowed it, making it seem as if it was a smaller resistance than reality.""",
            """The 100 kΩ resistor resulted in a much closer to expected result, 49.31 Ω, normal margin of error, because it struck a balance between load sensitivity and meter resolution. It was small enough to create a distinct voltage drop that the DMM was able to accurately capture.""",
            """With a 50 Ω resistor, the expectation would be that an equal voltage divided, or seeing the voltage being halved when measured on the DMM. However, that was not the case and this was due to a high current draw as a result of the low resistance. This caused the function generator to drive harder to maintain the chosen output amplitude and keeping the function generator’s output voltage higher, resulting in an artificially lower resistance.""",
            """The biggest hurdle I ran into was making sense of the function generator’s internal resistance calculations. Initially, I didn’t understand why the 1 MΩ and 470 kΩ loads gave me 0 Ω and 33 Ω, or why the 50 Ω load calculated out to only 7.86 Ω instead of the 50 Ω listed on the datasheet. What finally clicked was realizing that the huge resistors barely caused any voltage drop, meaning the tiny change was either lost in the meter’s resolution or drastically magnified by the math. At the same time, I learned that the 50 Ω load drew enough current to trigger the generator’s internal buffering, keeping the voltage higher than expected. This allowed the following work with the different waveforms to make much more sense.""",
        ],
    },
    {
        "name": "score separation",
        "criterion": 2,
        # The first five are clearly AI-generated comparison texts; the last
        # five are human-written paragraphs reused from the submitted papers.
        # run_eval.py preserves this order in every trial for the averages.
        "texts": [
            "The implementation of a reliable measurement system requires careful calibration, systematic observation, and consistent documentation. By controlling the relevant variables and repeating the procedure, a researcher can distinguish random variation from a meaningful pattern in the results.",
            "Digital tools have transformed the way people communicate, learn, and organize information. Although these tools improve efficiency, their benefits depend on responsible use, thoughtful evaluation, and an awareness of the limitations built into every system.",
            "A sustainable solution should address both the immediate problem and the conditions that produced it. Short-term action may reduce visible symptoms, but long-term improvement requires examining the underlying causes and measuring whether the intervention produces durable results.",
            "Effective collaboration depends on clear goals, defined responsibilities, and regular opportunities for feedback. When participants understand how their work contributes to a shared outcome, the group can identify problems earlier and make adjustments before small disagreements become major obstacles.",
            "The relationship between technology and society is not one-directional. People design tools according to their needs and assumptions, while those tools influence later decisions, habits, and expectations. Understanding this relationship requires examining both technical performance and human consequences.",
            "The 100 kΩ resistor resulted in a much closer to expected result, 49.31 Ω, normal margin of error, because it struck a balance between load sensitivity and meter resolution. It was small enough to create a distinct voltage drop that the DMM was able to accurately capture.",
            "With a 50 Ω resistor, the expectation would be that an equal voltage divided, or seeing the voltage being halved when measured on the DMM. However, that was not the case and this was due to a high current draw as a result of the low resistance. This caused the function generator to drive harder to maintain the chosen output amplitude and keeping the function generator’s output voltage higher, resulting in an artificially lower resistance.",
            "The biggest hurdle I ran into was making sense of the function generator’s internal resistance calculations. Initially, I didn’t understand why the 1 MΩ and 470 kΩ loads gave me 0 Ω and 33 Ω, or why the 50 Ω load calculated out to only 7.86 Ω instead of the 50 Ω listed on the datasheet. What finally clicked was realizing that the huge resistors barely caused any voltage drop, meaning the tiny change was either lost in the meter’s resolution or drastically magnified by the math.",
            "When applying a -1 V DC offset, an inverse shift in the DC domain is produced while the AC domain remains unchanged.",
            "When the trigger slope is changed to a Negative Slope on the oscilloscope, the waveform display shifts phase. Instead of the sine wave starting its trace upward from the zero-volt trigger level crossing on the left side of the screen, the waveform starts its trace downward from the exact same trigger point. The trigger crossing point dictates where the sweep begins rendering the signal.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across the score range: AI-like, human-like, and
        # borderline. The run determines whether all three labels are reachable.
        "texts": [
            "The implementation of a reliable measurement system requires careful calibration, systematic observation, and consistent documentation. By controlling the relevant variables and repeating the procedure, a researcher can distinguish random variation from a meaningful pattern in the results.",
            "With the much large resistance values (1 MΩ, 470 kΩ, 100 kΩ) there was little to no current being pulled, resulting in almost no voltage drop. With a low resistance of only 50 Ω, there was a noticeable voltage drop measured, resulting in lower voltage being measured than what the calculations tell us to expect.",
            "Sometimes a result looks convincing at first because the numbers seem to point in one direction. Looking more closely can reveal uncertainty, especially when the measurement is close to the instrument’s limits or when the explanation depends on assumptions that have not been tested.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # Each trial submits five fresh items, appeals each returned content_id,
        # and checks the appeal response plus the audit-log status.
        "appeals": [
            {"text": "I am asking for a review because this result does not match my experience writing this paragraph.", "reasoning": "I wrote this submission myself and want the decision reviewed."},
            {"text": "The measurement may not capture the context behind this submission, so I am requesting a second look.", "reasoning": "Please review the decision and the evidence recorded for this content."},
            {"text": "This result seems uncertain to me, and I would like a person to examine it.", "reasoning": "I am appealing because the automated result may be mistaken."},
            {"text": "The wording reflects my own notes and should be reviewed before any action is taken.", "reasoning": "Please place this item under review and preserve my explanation."},
            {"text": "I want to challenge this decision so that the original submission remains auditable.", "reasoning": "I am requesting an appeal and a recorded review of this decision."},
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty_1"},
            {"text": "   ", "creator_id": "eval_bad_empty_2"},
            {"creator_id": "eval_bad_missing_1"},
            {"creator_id": "eval_bad_missing_2"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "word " * 2001, "creator_id": "eval_bad_huge_1"},
            {"text": "long " * 2001, "creator_id": "eval_bad_huge_2"},
            {"text": "x" * 10001, "creator_id": "eval_bad_huge_3"},
            {"text": "text " * 2500, "creator_id": "eval_bad_huge_4"},
            {"text": "large " * 2000, "creator_id": "eval_bad_huge_5"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        appeals = scenario.get("appeals")

        if sum(bool(value) for value in (texts, bodies, appeals)) > 1:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has more than one "
                f"scenario input type — pick one"
            )
            continue

        if appeals:
            for j, appeal in enumerate(appeals, 1):
                if not isinstance(appeal, dict):
                    problems.append(f"scenario {i}, appeal {j} is not a dict")
                    continue
                if not isinstance(appeal.get("text"), str) or not appeal.get("text", "").strip():
                    problems.append(f"scenario {i}, appeal {j} has no usable text")
                if not isinstance(appeal.get("reasoning"), str) or not appeal.get("reasoning", "").strip():
                    problems.append(f"scenario {i}, appeal {j} has no usable reasoning")
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
