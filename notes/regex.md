# Chapter 2 - Section 2.1: Regular Expressions

## Introduction to Regular Expressions (Regex)

*   **Definition:** A **regular expression** (regex) is a language for specifying text search strings. Formally, it's an algebraic notation for characterizing a set of strings.
*   **Purpose:** Extremely useful for finding patterns within a text **corpus** (a single document or a collection).
*   **Tools:** Used in many programming languages, command-line tools (`grep`), and text editors (`vim`, `emacs`).
*   **Functionality:** A regex search function scans the corpus and returns strings (or lines containing strings) that match the specified pattern. Can return first match or all matches.
*   **Notation:** Regex patterns are often delimited by slashes (e.g., `/pattern/`), but the slashes are *not* part of the pattern itself.
*   **Variants:** Regex implementations can vary slightly (this text uses "extended regular expressions"). Testing tools are helpful.

## Basic Regular Expression Patterns

*   **Literal Characters & Concatenation:** The simplest regex consists of literal characters matched in sequence.
    *   `/woodchuck/` matches the exact substring "woodchuck".
    *   `/a/` matches the character "a".
    *   `/!/` matches the character "!".
*   **Case Sensitivity:** Regex matching is typically case-sensitive.
    *   `/s/` matches "s" but not "S".
    *   `/woodchucks/` does not match "Woodchucks".

## Character Sets, Ranges, and Negation (`[]`)

*   **Disjunction (`[]`):** Square brackets specify a match for *any one* character from the set listed inside.
    *   `/[wW]/` matches either "w" or "W". -> `/[wW]oodchuck/` matches "woodchuck" or "Woodchuck".
    *   `/[abc]/` matches "a", "b", or "c".
    *   `/[1234567890]/` matches any single digit.
*   **Ranges (`-`):** Inside square brackets, a dash specifies a range of characters.
    *   `/[A-Z]/` matches any uppercase letter.
    *   `/[a-z]/` matches any lowercase letter.
    *   `/[0-9]/` matches any single digit (equivalent to `/[1234567890]/`).
    *   `/[2-5]/` matches "2", "3", "4", or "5".
*   **Negation (`^`):** When `^` is the *first* character inside square brackets, it negates the set, matching any character *except* those listed.
    *   `/[^a]/` matches any character except "a".
    *   `/[^A-Z]/` matches any character that is *not* an uppercase letter.
    *   `/[^Ss]/` matches any character except "S" or "s".
    *   `/[^.]/` matches any character except a period.
    *   **Caution:** If `^` is *not* the first character, it usually matches a literal caret: `/[e^]/` matches "e" or "^".

    🤔 **Understanding `^`:** The meaning of `^` depends on context!
    *   Inside `[` and *at the beginning*: Negation (match anything *not* in the set).
    *   Inside `[` but *not* at the beginning: Literal caret character `^`.
    *   *Outside* `[` (see Anchors below): Start of line.

## Quantifiers (Repetition)

*   **Optional (`?`):** Matches the preceding element *zero or one* time.
    *   `/woodchucks?/` matches "woodchuck" or "woodchucks".
    *   `/colou?r/` matches "color" or "colour".
*   **Kleene Star (`*`):** Matches the preceding element *zero or more* times.
    *   `/a*/` matches "" (empty string), "a", "aa", "aaaa", etc.
    *   `/baaa*!/` matches "baa!", "baaa!", "baaaa!", etc. (at least two 'a's).
    *   `/[ab]*/` matches "", "a", "b", "aa", "bb", "ab", "ba", "abab", etc.
    *   `/[0-9][0-9]*/` matches one digit followed by zero or more digits (i.e., any integer).

    💡 **Tip: The `*` Kleene Star Trap:** Remember `*` means *zero* or more. This can sometimes lead to unexpected matches, like matching an empty string at the beginning of a line if the pattern allows it. `/a*/` will match in the string "bbb" (it matches the zero 'a's at the start).

*   **Kleene Plus (`+`):** Matches the preceding element *one or more* times.
    *   `/a+/` matches "a", "aa", "aaaa", etc. (but *not* the empty string).
    *   `/baa+!/` matches "baa!", "baaa!", "baaaa!", etc. (equivalent to `/baaa*!/` - requires at least two 'a's).
    *   `/[0-9]+/` matches one or more digits (a common way to find numbers).

    💡 **Tip: `*` vs `+`:**
    *   `X*` = Match X zero or more times.
    *   `X+` = Match X one or more times.
    *   `X+` is roughly equivalent to `XX*`.

## Wildcard (`.`)

*   **Period (`.`):** Matches *any single character* (except newline/carriage return).
    *   `/beg.n/` matches "begin", "beg'n", "begun", etc.
*   **Combining with `*`:** `.*` matches *any sequence of zero or more characters*.
    *   `/aardvark.*aardvark/` matches lines containing "aardvark" appearing twice, with anything (or nothing) in between.

    💡 **Tip: Escaping Special Characters:** Since `.` is special (a wildcard), how do you match an actual period? You need to **escape** it with a backslash: `\.`. This applies to other regex metacharacters like `*`, `+`, `?`, `[`, `]`, `^`, `$`, `\`. So, `/a\.b/` matches "a.b" literally.

## Anchors

*   **Definition:** Anchors tie the regex pattern to specific positions in the string/line. They don't match characters themselves, but *positions*.
*   **Start of Line (`^`):** Matches the beginning of a line.
    *   `/^The/` matches "The" only if it's at the start of the line.
    *   `/^$/` matches an empty line.
*   **End of Line (`$`):** Matches the end of a line.
    *   `/dog$/` matches "dog" only if it's at the end of the line.
    *   `/^The dog\.$/` matches a line containing *only* "The dog." (note the escaped period `\.`).
*   **Word Boundary (`\b`):** Matches the position between a word character and a non-word character, or start/end of string if it begins/ends with a word character.
    *   **Word Characters:** Usually letters, digits, and underscore (`[a-zA-Z0-9_]`).
    *   **Non-Word Characters:** Anything else (spaces, punctuation, etc.).
    *   `/\bthe\b/` matches the whole word "the" (e.g., in "the dog") but not as part of another word (e.g., "other").
    *   `/\b99\b/` matches "99" in "There are 99 bottles" (space before, end of string after) and in "$99" ($ is non-word char), but not in "299" (2 is a word char).
*   **Non-Word Boundary (`\B`):** Matches any position that is *not* a word boundary.
    *   `/\Bthe\B/` would match "the" inside "other" but not the standalone word "the".

    🤔 **Understanding Word Boundaries `\b`:** Think of `\b` as matching the *transition point* between a "word" character (like 't' or '5') and a "non-word" character (like ' ', '$', or the start/end of the line). It's useful for matching whole words.

## 2.1.2 Disjunction, Grouping, and Precedence

*   **Disjunction (`|`):** The pipe symbol `|` acts as an OR operator, matching *either* the expression to its left *or* the expression to its right.
    *   `/cat|dog/` matches the string "cat" or the string "dog".
    *   **Important Distinction:** `/[catdog]/` matches *single characters* 'c', 'a', 't', 'd', 'o', 'g'. `cat|dog` matches the *entire strings* "cat" or "dog".

    💡 **Tip: `|` vs `[]`**
    *   `[]` = OR for **single characters** (e.g., `/[abc]/` means 'a' OR 'b' OR 'c').
    *   `|` = OR for **sequences/patterns** (e.g., `/cat|dog/` means 'cat' OR 'dog').

*   **Grouping (`()`):** Parentheses `()` are used to group parts of a regex pattern.
    *   **Purpose 1: Scoping Disjunction:** Limits the scope of the `|` operator.
        *   `/guppy|ies/` matches "guppy" or "ies" (due to precedence).
        *   `/gupp(y|ies)/` matches "guppy" or "guppies". The `|` only applies to 'y' and 'ies' within the group.
    *   **Purpose 2: Scoping Quantifiers:** Applies quantifiers (`*`, `+`, `?`) to a whole sequence instead of just the preceding character.
        *   `/Column [0-9]+ */` matches "Column ", one or more digits, and then *zero or more spaces*. The `*` only applies to the space.
        *   `/(Column [0-9]+ *)*/` matches *zero or more repetitions* of the entire pattern "Column, followed by digits, followed by optional spaces".

*   **Operator Precedence:** Determines the order in which regex operations are evaluated (similar to mathematical operators).
    *   **Hierarchy (Highest to Lowest):**
        1.  `()` : Parentheses (Grouping)
        2.  `* + ? {}` : Counters / Quantifiers
        3.  `abc`, `^`, `$` : Sequences and Anchors
        4.  `|` : Disjunction
    *   **Examples:**
        *   `/the*/`: `*` has higher precedence than sequence, so it applies only to `e`. Matches "th", "the", "thee", "theeee", etc.
        *   `/the|any/`: Sequence has higher precedence than `|`. Matches "the" or "any". It does *not* match "theny" or "thany". Parentheses would be needed for that: `/th(e|any)/`.

*   **Greedy Matching:** By default, quantifiers (`*`, `+`) are **greedy**. They try to match the *longest possible* string that satisfies the pattern.
    *   Example: Applying `/[a-z]*/` to "once upon a time". It *could* match "", "o", "on", "onc", or "once". Greediness means it will match the longest possibility: "once".

*   **Non-Greedy Matching (`*?`, `+?`):** Appending `?` after a quantifier (`*` or `+`) makes it **non-greedy** (or "lazy"). It matches the *shortest possible* string.
    *   `*?`: Non-greedy version of `*` (zero or more, shortest match).
    *   `+?`: Non-greedy version of `+` (one or more, shortest match).

    🤔 **Understanding Greediness:** Imagine `.*` between two patterns, like `/START.*END/` applied to "START one END two END". The greedy `.*` will match " one END two ". The non-greedy `.*?` in `/START.*?END/` would match just " one ". It stops at the *first* possible "END".

## 2.1.3 A Simple Example: Matching "the"

This section illustrates the iterative process of refining a regex pattern.

*   **Goal:** Find instances of the English article "the".

*   **Attempt 1:** `/the/`
    *   **Problem:** Misses capitalized "The" at the start of sentences. This is a **False Negative**.

*   **Attempt 2:** `/[tT]he/` (Uses character set `[tT]` for case-insensitivity)
    *   **Problem:** Incorrectly matches "the" embedded within other words like "other" or "there". These are **False Positives**.

*   **Attempt 3:** `/\b[tT]he\b/` (Uses word boundaries `\b`)
    *   **Solution:** `\b` ensures that the pattern only matches when "the" (case-insensitive) appears as a whole word, separated from adjacent characters by a non-word character (like space, punctuation, or start/end of line).

*   **Key Error Types in Pattern Matching (and NLP generally):**
    *   **False Positives (FP):** Strings that the pattern matched, but *should not* have matched (e.g., matching "there" when looking for "the"). Type I error.
    *   **False Negatives (FN):** Strings that the pattern *failed* to match, but *should* have matched (e.g., missing "The" when looking for "the"). Type II error.

*   **Goal of Improving NLP Applications:** Reduce overall error rate by:
    *   **Increasing Precision:** Minimizing False Positives. (Making sure the matches you find are actually correct).
    *   **Increasing Recall:** Minimizing False Negatives. (Making sure you find all the correct matches you *should* have found).

    💡 **Tip: Iterative Refinement:** Building good regex patterns (and many NLP models) is often a process of:
    1.  Write an initial pattern.
    2.  Test it on data.
    3.  Identify False Positives (over-generation) and False Negatives (under-generation).
    4.  Refine the pattern to address the errors.
    5.  Repeat steps 2-4.

## 2.1.4 More Operators

*   **Character Class Aliases:** Shorthands for common character sets.

    | Alias | Expansion         | Meaning                           | Example Match      |
    | :---- | :---------------- | :-------------------------------- | :----------------- |
    | `\d`  | `[0-9]`           | Any digit                         | `5` in "Party of 5"  |
    | `\D`  | `[^0-9]`          | Any non-digit                     | `B` in "Blue moon"   |
    | `\w`  | `[a-zA-Z0-9_]`    | Any alphanumeric or underscore    | `Daiyu`            |
    | `\W`  | `[^a-zA-Z0-9_]`   | Any non-alphanumeric              | `!` in "!!!!"      |
    | `\s`  | `[ \r\t\n\f]`     | Whitespace (space, return, tab, newline, form feed) | ` ` in "in Concord"  |
    | `\S`  | `[^ \r\t\n\f]`    | Any non-whitespace character      | `i` in "in Concord"  |

    💡 **Tip `\w` vs `\b`:** Remember `\w` matches a *character* that is part of a "word". `\b` matches a zero-width *position* that is a word boundary. They are often used together, like `\b\w+\b` to match a whole word.

*   **Exact/Ranged Quantifiers (`{}`):** Curly braces specify exact numbers or ranges for the preceding element.

    | Quantifier | Meaning                                          |
    | :--------- | :----------------------------------------------- |
    | `{n}`      | Exactly `n` occurrences.                         |
    | `{n,m}`    | Between `n` and `m` occurrences (inclusive).     |
    | `{n,}`     | At least `n` occurrences.                        |
    | `{,m}`     | Up to `m` occurrences (including zero). *Note: Less common/supported in some versions.* |
    | `*`        | Same as `{0,}`                                   |
    | `+`        | Same as `{1,}`                                   |
    | `?`        | Same as `{0,1}`                                  |

    *   Example: `/a\.{24}z/` matches 'a', followed by exactly 24 periods, followed by 'z'.

*   **Escaping Special Characters (`\`):** To match characters that have special meaning in regex, precede them with a backslash `\`.
    *   `\.` matches a literal period (`.`)
    *   `\*` matches a literal asterisk (`*`)
    *   `\?` matches a literal question mark (`?`)
    *   `\[` matches a literal open square bracket (`[`)
    *   `\\` matches a literal backslash (`\`)
    *   Also used for non-printing characters:
        *   `\n` : Newline
        *   `\t` : Tab

## 2.1.5 A More Complex Example: Finding Computer Specs

Illustrates building regex for specific formats like prices and disk sizes. Goal: Find computers with "at least 6 GHz and 500 GB of disk space for less than $1000".

*   **Regex for Prices (Iterative Refinement):**
    1.  **Basic Dollars:** `/$[0-9]+/`
        *   Matches `$` followed by one or more digits.
    2.  **Adding Cents (Initial thought, flawed):** `/$[0-9]+\.[0-9][0-9]/`
        *   Requires exactly two digits after the decimal. Doesn't match `$199`.
    3.  **Making Cents Optional:** `/$[0-9]+(\.[0-9][0-9])?/`
        *   Uses `()` to group the decimal part (`\.` for literal dot, `[0-9][0-9]` for two digits).
        *   Uses `?` to make the entire group optional (zero or one occurrence).
    4.  **Adding Boundaries:** `/(^|\W)$[0-9]+(\.[0-9][0-9])?\b/`
        *   `\b`: Word boundary at the end to avoid matching inside another number (e.g., `$199.99` in `$199.999`).
        *   `( ^|\W )`: Matches either the start of the line (`^`) OR a non-word character (`\W`) before the `$`. Prevents matching `abc$199.99`.

        🤔 **Understanding `(^|\W)`:** This ensures the price isn't preceded by a letter, number, or underscore. It allows the price to be at the start of the line OR follow a space, punctuation, etc.

        💡 **Tip: Context of `$`:** The `$` character has multiple meanings:
        *   Inside a pattern (not at the end): Matches a literal dollar sign (as in `/$[0-9]+/`). Most parsers figure this out from context.
        *   At the end of a pattern: Matches the end of the line anchor (as in `/end$/`).
        *   Inside `[]`: Usually just a literal dollar sign `/[abc$]/`.

    5.  **Limiting Dollar Amount (for < "$1000"): /(ˆ|\W)$[0-9]{0,3}(\.[0-9][0-9])?\b/ 
    *   Replaces `[0-9]+` with `[0-9]{1,3}` to match 1 to 3 digits for the dollar amount.
    *   *Note:* The text used `{0,3}` which could match just `$`, potentially needing further refinement (e.g., ensuring at least one digit if no cents, or handling `$0`). The pattern `/^\$[0-9]{1,3}(\.[0-9]{2})?\b/` might be closer but depends on exact requirements. Also, regex alone *cannot* check if the value is truly "< 1000" (e.g., it matches `$999` but also `$100` and `$1`). This usually requires extracting the match and then using programming logic to check the value.

*   **Regex for Disk Space:**
    *   Goal: Match patterns like `500 GB`.
    *   **Number part (integer or decimal):** `[0-9]+(\.[0-9]+)?`
        *   One or more digits `[0-9]+`.
        *   Optionally `?`, a group `()` containing a literal dot `\.` followed by one or more digits `[0-9]+`.
    *   **Optional spaces:** ` *` (zero or more spaces).
    *   **Units (GB, Gigabyte, Gigabytes):** `(GB|[Gg]igabytes?)`
        *   Uses `()` for grouping and `|` for disjunction.
        *   Matches literal "GB" OR...
        *   Matches "Gigabyte" or "gigabyte" (using `[Gg]`) followed by an optional 's' (`s?`).
    *   **Word Boundaries:** `\b` at start and end.
    *   **Combined:** `/\b[0-9]+(\.[0-9]+)? *(GB|[Gg]igabytes?)\b/`

    💡 **Tip: Regex Limitations:** Regex is powerful for finding *patterns*, but not for understanding *semantics* or doing *calculations*.
    *   The price regex finds strings that *look like* prices under $1000, but doesn't actually *compare* the numeric value.
    *   Similarly, modifying the disk space regex to match *only* values "> 500" is complex and often better handled by extracting the number found by the regex and checking it programmatically.

## 2.1.6 Substitution, Capture Groups, and ELIZA

*   **Substitution:** Replacing text that matches a regex pattern with a different string.
    *   **Common Syntax:** `s/regex_pattern/replacement_string/` (used in Python, sed, vim, etc.).
    *   **Example:** `s/colour/color/` replaces "colour" with "color".

*   **Capture Groups (`()`):** Parentheses `()` in a regex pattern serve two main purposes:
    1.  **Grouping:** Group parts of the pattern for operators like `|` or quantifiers (`*`, `+`, `?`, `{}`).
    2.  **Capturing:** Store the substring that matched the part of the pattern inside the parentheses into a numbered register (memory).

*   **Backreferences (`\1`, `\2`, etc.):** Referencing the text matched by a capture group.
    *   `\1` refers to the text matched by the *first* capture group in the regex.
    *   `\2` refers to the text matched by the *second* capture group, and so on.
    *   **Use in Substitution:** Allows using the captured text in the replacement string.
        *   Example: `s/([0-9]+)/<\1>/` finds one or more digits `([0-9]+)`, captures them (e.g., "35"), and replaces the match with the captured text surrounded by angle brackets (e.g., "<35>").
    *   **Use in Matching:** Enforces that the same captured text appears later in the pattern.
        *   Example: `/the (.*)er they were, the \1er they will be/`
            *   `(.*)` captures any sequence of characters (e.g., "bigg").
            *   `\1` requires that the *same sequence* ("bigg") appears later in the string.
            *   Matches: "the bigger they were, the bigger they will be".
            *   Does NOT match: "the bigger they were, the faster they will be".
        *   Example: `/the (.*)er they (.*), the \1er we \2/`
            *   `(.*)` is group 1, `(.*)` is group 2.
            *   `\1` refers to group 1's match, `\2` refers to group 2's match.
            *   Matches: "the faster they ran, the faster we ran".
            *   Does NOT match: "the faster they ran, the faster we ate".

    💡 **Tip: Backreference Numbering:** Groups are numbered based on the order of their *opening* parenthesis `(`.

*   **Non-Capturing Groups (`(?:...)`):** Allows grouping for scope/precedence *without* capturing the matched text into a register.
    *   **Syntax:** `(?:pattern)`
    *   **Purpose:** Useful when you need parentheses for grouping (e.g., with `|` or quantifiers) but don't intend to refer back to the matched text using a backreference (`\1`, `\2`, etc.). This avoids "using up" a capture group number.
    *   **Example:** `/(?:some|a few) (people|cats) like some \1/`
        *   `(?:some|a few)`: Groups "some" or "a few" but doesn't capture.
        *   `(people|cats)`: Groups and *captures* "people" or "cats" as group `\1`.
        *   Matches: "some cats like some cats", "a few people like some people".
        *   Does NOT match: "some cats like some some" (because `\1` must match the captured group, which was "cats").

*   **ELIZA Chatbot Example:**
    *   An early NLP program simulating a Rogerian psychologist.
    *   Worked using a **cascade** (ordered sequence) of regex substitutions with capture groups.
    *   **Steps:**
        1.  Uppercase input.
        2.  Apply pronoun swapping rules (e.g., `s/MY/YOUR/g`, `s/I'M/YOU ARE/g`).
        3.  Apply pattern-based response rules, often using capture groups to incorporate user input into the response.
            *   `s/.* YOU ARE (depressed|sad) .*/I AM SORRY TO HEAR YOU ARE \1/`
            *   `s/.* all .*/IN WHAT WAY/`
            *   `s/.* always .*/CAN YOU THINK OF A SPECIFIC EXAMPLE/`
    *   Rule **ranking/order** is important because multiple rules might match.

## 2.1.7 Lookahead Assertions

*   **Purpose:** Lookahead allows checking for a pattern *after* the current position in the string **without consuming characters** (i.e., without advancing the main regex engine's position in the string). It's like "peeking ahead".
*   **Zero-Width:** Lookahead assertions match a *position*, not characters. They succeed or fail, but don't "use up" any characters in the string being matched.
*   **Positive Lookahead (`(?=...)`):**
    *   **Syntax:** `(?=pattern)`
    *   **Meaning:** Asserts that `pattern` *must* match immediately following the current position, but doesn't capture `pattern` or move the pointer. Succeeds if the `pattern` is found ahead, fails otherwise.
    *   **Use Case:** Match something only if it's followed by something else. E.g., `/\d+(?= dollars)/` would match the number in "100 dollars" but not in "100 pounds".
*   **Negative Lookahead (`(?!...)`):**
    *   **Syntax:** `(?!pattern)`
    *   **Meaning:** Asserts that `pattern` *must NOT* match immediately following the current position. Also zero-width. Succeeds if the `pattern` is *not* found ahead, fails otherwise.
    *   **Use Case:** Exclude certain cases or rule out specific patterns.
    *   **Example:** `/^(?!Volcano)[A-Za-z]+/`
        *   `^`: Anchor to start of line.
        *   `(?!Volcano)`: Negative lookahead - asserts that the string "Volcano" does NOT immediately follow.
        *   `[A-Za-z]+`: Matches one or more letters (a word).
        *   **Result:** Matches any word at the start of the line *except* for the word "Volcano".

    🤔 **Understanding Lookahead vs. Non-Capturing Groups:**
    *   **Non-Capturing Group `(?:...)`:** *Matches* and *consumes* characters, but doesn't store them in a backreference. The pointer advances.
    *   **Lookahead `(?=...)` or `(?!...)`:** *Checks* for a pattern ahead but does **not** consume characters and does **not** store them. The pointer does **not** advance based on the lookahead match/non-match. It's purely an assertion about what follows.

# Section 2.2: Words

## Defining "Word"

*   The definition of a "word" is not always straightforward and depends on the specific NLP task.
*   **Corpus (pl. Corpora):** A computer-readable collection of text or speech used for analysis. Examples:
    *   **Brown Corpus:** ~1 million words, written English samples (news, fiction, etc.), 1960s.
    *   **Switchboard Corpus:** ~3 million words, telephone conversations, 1990s.

## Complications in Defining Words

*   **Punctuation:** Should punctuation marks (`,`, `.`, `!`, `?`) count as words?
    *   **Task Dependent:** Sometimes excluded, sometimes treated as separate words.
    *   **Importance:** Crucial for boundaries (periods, commas) and meaning (question/exclamation marks). Useful for tasks like Part-of-Speech tagging, parsing, speech synthesis.
*   **Spoken Language:** Introduces additional complexities.
    *   **Utterance:** The spoken equivalent of a sentence.
    *   **Disfluencies:** Common in speech, interrupting the flow.
        *   **Fragments:** Broken-off words (e.g., `main-` in "main- mainly").
        *   **Fillers / Filled Pauses:** Words like `uh`, `um`.
    *   **Handling Disfluencies:**
        *   Task-dependent: Sometimes removed (e.g., for clean transcription), sometimes kept.
        *   **Reasons to Keep:** Can be predictive in speech recognition (signal restarts), cues for speaker identification, may even carry distinct meanings (`uh` vs `um`).

    💡 **Tip: Don't Discard Disfluencies Automatically:** While they might seem like noise, disfluencies contain useful information for certain speech-related tasks. Their presence and type can be predictive features.

## Key Concepts: Types, Instances, Forms, Lemmas

*   **Word Types:** The number of *distinct* words in a corpus. Represents the size of the **vocabulary** (`|V|`).
*   **Word Instances (or Tokens*):** The *total* number of words in a corpus (`N`).
    *   Example Sentence: "They picnicked by the pool, then lay back on the grass and looked at the stars." (Ignoring punctuation)
        *   **Instances (N):** 16
        *   **Types (|V|):** 14 ("the" appears 3 times, counts as 1 type)
    *   ***Note:** The text mentions that "token" is increasingly reserved for outputs of *subword* tokenization (like BPE), so "instance" is preferred for counting running words.

*   **Capitalization:** Does "They" count as the same type as "they"?
    *   **Task Dependent:**
        *   **Ignore Case:** Often done for tasks where word sequence matters most (e.g., speech recognition). Reduces vocabulary size.
        *   **Preserve Case:** Important for tasks where capitalization is a feature (e.g., Named Entity Recognition - distinguishing "Apple" the company from "apple" the fruit).
    *   Common practice: Maintain cased and uncased versions of models/data.

*   **Vocabulary Growth - Heaps' Law / Herdan's Law:** Describes the relationship between the number of word types (`|V|`) and word instances (`N`) in a corpus.
    *   Formula: `|V| = k * N^β`
    *   `k`, `β` are positive constants depending on the corpus/genre.
    *   `0 < β < 1` (typically 0.67 - 0.75 for large English corpora).
    *   **Implication:** The vocabulary size grows sublinearly with the corpus size (faster than the square root, but slower than linear). Adding more text introduces *new* words at a decreasing rate.

*   **Wordform vs. Lemma:**
    *   **Wordform:** The full inflected or derived surface form of a word as it appears in text (e.g., "cat", "cats", "running", "ran").
    *   **Lemma:** A canonical or dictionary form representing a set of wordforms. Typically the base stem + major part-of-speech (e.g., `cat` is the lemma for "cat" and "cats"; `run` is the lemma for "run", "running", "ran").
    *   **Relevance:** Lemmatization is crucial for morphologically rich languages. For many English tasks, working with wordforms is sufficient. Dictionary headwords roughly approximate lemmas.
    *   **Usage in Book:** "Word" usually refers to **wordform** unless specified otherwise.

    🤔 **Understanding Lemma vs. Wordform:** Think of the **lemma** as the dictionary entry headword (like `run`) and **wordforms** as all the variations you might find in actual text (`run`, `runs`, `ran`, `running`).

## Beyond Words: Tokenization

*   Modern NLP (especially neural models) often doesn't use words as the fundamental unit.
*   **Tokenization:** The process of breaking input text into units called **tokens**.
*   **Tokens:** Can be words, punctuation, or even *parts* of words (subword units).
*   Subword tokenization (e.g., BPE algorithm) will be discussed later.

# Section 2.3: Corpora

## The Importance of Context in Language Data

*   Text/speech is not generated in a vacuum. It's produced by specific people, in a specific language/dialect, at a specific time/place, for a specific purpose.
*   Understanding this context is crucial for developing robust and fair NLP algorithms.

## Dimensions of Variation in Corpora

1.  **Language:**
    *   Huge diversity globally (~7000 languages - Ethnologue).
    *   NLP often has a bias towards English and languages of large industrialized nations.
    *   **Critical Need:** Test and develop algorithms on a wider variety of languages, especially those with different linguistic properties.

2.  **Variety / Dialect:**
    *   Most languages have multiple varieties (regional, social).
    *   Example: **African American English (AAE) / African American Vernacular English (AAVE)** vs. **Mainstream American English (MAE)**.
    *   AAE features (e.g., `iont` for "I don't", `talmbout` for "talking about") impact basic NLP tasks like word segmentation.
    *   NLP tools must be functional across different varieties to be equitable and effective.

3.  **Code Switching:**
    *   Using multiple languages within a single conversation or text.
    *   Very common globally.
    *   Examples provided: Spanish/English, Hindi/English.
    *   NLP systems need to handle mixed-language input.

4.  **Genre:**
    *   The type or style of text/speech significantly impacts linguistic features.
    *   Examples: Newswire, fiction, scientific articles, Wikipedia, spoken conversations (phone, meetings), medical notes, legal text, social media, etc.
    *   Algorithms trained on one genre may not perform well on another.

5.  **Demographics:**
    *   Characteristics of the speaker/writer influence language use:
        *   Age
        *   Gender
        *   Race
        *   Socioeconomic Class
    *   These factors can correlate with linguistic patterns.

6.  **Time:**
    *   Language evolves over time.
    *   Historical corpora exist for studying language change.
    *   NLP models might need to account for temporal differences if processing historical text or analyzing trends.

💡 **Tip: Situated Language Matters:** Always consider *where* your training data comes from and *where* your NLP tool will be used. A model trained solely on 1990s newswire might struggle with 2020s Twitter data containing AAE features and modern slang, or perform poorly on medical dictations. This variation is a major challenge and area of research in NLP.

## Documenting Corpora: Datasheets & Data Statements

*   To address the need for context, corpus creators should provide documentation.
*   **Datasheet / Data Statement:** A document specifying key properties of a dataset. Essential for transparency and responsible use.
*   **Key Information Included:**
    *   **Motivation:** Why collected? By whom? Funding?
    *   **Situation:** When/where was the text produced? Task involved? Spoken/written? Dialogue/monologue? Social media?
    *   **Language Variety:** Specific language, dialect, region.
    *   **Speaker Demographics:** Age, gender, etc. (if available/relevant).
    *   **Collection Process:** Data size? Sampling method? Consent obtained? Pre-processing steps? Metadata availability?
    *   **Annotation Process:** (If annotated) What labels? Annotator demographics/training? Annotation procedure?
    *   **Distribution:** Copyright/IP restrictions? How to access?

🤔 **Understanding Datasheets:** Think of them like nutrition labels for datasets. They tell you what's inside, how it was made, and any potential limitations or biases, helping researchers and developers use the data responsibly and understand the context of models trained on it.

# Section 2.5: Word and Subword Tokenization

## Introduction to Tokenization

*   **Tokenization:** The fundamental task of segmenting running text into individual units called **tokens**.
*   **Tokens:** Can be words, punctuation, numbers, or, increasingly, **subword units** (parts of words or characters).
*   **Goal:** Prepare text for downstream NLP algorithms.

## Two Main Approaches to Tokenization

1.  **Top-down (Rule-based) Tokenization:**
    *   Define a standard for what constitutes a token (often word-level).
    *   Implement explicit rules (often using regular expressions) to achieve this segmentation.
    *   Historically common, still used for specific tasks or when strict adherence to linguistic rules is needed.

2.  **Bottom-up (Statistical/Data-Driven) Tokenization:**
    *   Use statistics derived from the frequency of character sequences in the data.
    *   Automatically derive a vocabulary of tokens, which often include frequent words and subword units for rarer words.
    *   More common now, especially for large neural network models. Creates **subword tokens**. (Detailed algorithms like BPE discussed later).

## Top-down (Rule-based) Tokenization Details

*   **Goal:** More sophisticated than simple splitting; aims to handle various linguistic phenomena correctly according to predefined rules.
*   **Common Requirements & Challenges:**
    *   **Keep Punctuation:** Often desired to separate punctuation (`,`, `.`) as distinct tokens for parsing or boundary detection, but *keep* internal punctuation (e.g., `m.p.h.`, `Ph.D.`, `AT&T`, `cap'n`).
    *   **Handle Complex Units:** Keep prices (`$45.55`), dates (`01/02/06`), URLs (`https://...`), hashtags (`#nlproc`), emails (`user@domain.com`) as single tokens.
    *   **Numbers:** Handle internal commas/spaces/periods differently depending on language conventions (e.g., English `555,500.50` vs. German `555 500,50`).
    *   **Clitics:** Expand contractions. A **clitic** is a morpheme that functions like a word but depends phonologically on another word (e.g., `'re`, `n't`). Examples: `what're` -> `what`, `are`; `doesn't` -> `does`, `n't`. Also occurs in other languages (French `j'ai`, `l'homme`).
    *   **Multiword Expressions (MWEs):** Some applications might treat phrases like `New York` or `rock 'n' roll` as single tokens (requires a predefined list/dictionary). Related to **Named Entity Recognition**.

*   **Example Standard: Penn Treebank (PTB) Tokenization:**
    *   Widely used standard, especially for linguistic corpora (like treebanks).
    *   Separates clitics (`doesn't` -> `does`, `n't`).
    *   Keeps hyphenated words together (`San Francisco-based`).
    *   Separates punctuation marks as distinct tokens (`,`, `.`, `"`).
    *   Example:
        *   Input: `"The San Francisco-based restaurant," they said, "doesn’t charge $10".`
        *   Output: `" The San Francisco-based restaurant , " they said , " does n’t charge $ 10 " .` (Spaces shown for clarity, often newlines).

*   **Implementation:**
    *   Typically uses deterministic algorithms based on **Regular Expressions** compiled into efficient **Finite State Automata (FSA)** for speed.
    *   Needs careful design to handle ambiguities (e.g., apostrophe in `book's` vs. `'The other class'` vs. `they're`).
    *   Example: NLTK's `nltk.regexp_tokenize` uses a complex regex pattern to handle abbreviations, hyphenated words, currency, ellipsis, and standard punctuation (Fig 2.12).

    💡 **Tip: Regex Complexity:** Writing robust rule-based tokenizers often requires complex, carefully ordered regular expressions to correctly handle the diverse patterns and ambiguities found in real text. Tools like NLTK provide pre-built, well-tested tokenizers.

*   **Challenges in Languages Without Spaces:**
    *   Languages like Chinese, Japanese, Thai don't use spaces to delimit words.
    *   Requires **Word Segmentation** algorithms.
    *   **Chinese:**
        *   Words are composed of characters (`hanzi`), each often a morpheme/syllable.
        *   Word definition is ambiguous; different standards exist (e.g., 3-word vs 5-word segmentation for "Yao Ming reaches the finals").
        *   Often more effective to process Chinese at the **character level** (treating each `hanzi` as a token) due to reasonable semantic granularity and avoidance of large/sparse word vocabularies.
    *   **Japanese & Thai:**
        *   Character level is often too small/granular.
        *   Requires word segmentation or, more commonly now, subword tokenization.

    🤔 **Understanding Segmentation Ambiguity:** The Chinese example highlights that even native speakers or linguists may disagree on the "correct" word boundaries, making rule-based segmentation difficult and favouring data-driven or character-level approaches.

## Transition to Subword Tokenization

*   While rule-based tokenizers handle many cases, subword tokenization (derived bottom-up) is increasingly preferred, especially for neural models, handling rare words, morphology, and languages like Japanese/Thai effectively.

# Section 2.5.2: Byte-Pair Encoding (BPE)

## Subword Tokenization: Motivation

*   **Problem:** Traditional word tokenization struggles with **unknown words** (Out-Of-Vocabulary - OOV). If a word appears in the test data but not the training data (e.g., test has "lower", training only had "low", "newer"), the system doesn't know how to handle it.
*   **Solution:** Use **subword** tokens. These are units smaller than words (often frequent character sequences or morphemes like "-er", "-est") derived automatically from the data.
*   **Benefit:** Any word, including unknown ones, can be represented as a sequence of known subword tokens (e.g., "lower" -> "low", "er"). In the worst case, any word can be represented as a sequence of individual characters, which are always in the initial vocabulary.
*   **Morphemes:** Subwords can sometimes correspond to **morphemes** (smallest meaning-bearing units, e.g., `un-`, `wash`, `-able` in `unwashable`), but they are often just frequent character sequences without inherent linguistic meaning.

## Common Subword Tokenization Algorithms

*   Most schemes have two components:
    1.  **Token Learner:** Analyzes a training corpus to induce a vocabulary of tokens (words and subwords).
    2.  **Token Segmenter:** Uses the learned vocabulary to segment new (test) sentences into tokens.
*   Widely used algorithms/libraries:
    *   **Byte-Pair Encoding (BPE):** Focus of this section (Sennrich et al., 2016).
    *   **Unigram Language Modeling:** (Kudo, 2018).
    *   **SentencePiece:** Library implementing both BPE and Unigram LM (Kudo and Richardson, 2018a). Often used synonymously with Unigram LM tokenization.

## Byte-Pair Encoding (BPE) Algorithm

*   **Type:** Bottom-up, data-driven tokenization.
*   **Goal:** Learn a vocabulary of tokens by iteratively merging frequent pairs of existing tokens.

### BPE Token Learner (`function BYTE-PAIR ENCODING`):

1.  **Initialization:**
    *   Start with a base **vocabulary** containing all individual characters present in the training corpus.
    *   Pre-process the corpus: Often split by whitespace initially. Add a special **end-of-word symbol** (e.g., `</w>`, ` `) to the end of each word. Represent words as sequences of characters plus this symbol.
    *   Count the frequency of each word in the training corpus.
2.  **Iteration:** Repeat `k` times (where `k` is a hyperparameter determining the number of merges/final vocab size):
    *   **Count Pairs:** Find the pair of adjacent tokens (symbols) that occurs most frequently across all words in the current corpus representation.
    *   **Merge:** Create a new token by concatenating the most frequent pair (e.g., `e` + `r` -> `er`).
    *   **Add to Vocabulary:** Add the newly merged token to the vocabulary.
    *   **Replace in Corpus:** Replace *all* occurrences of the original adjacent pair in the corpus representation with the new merged token.
3.  **Output:** The final vocabulary consists of the initial characters plus the `k` newly created merged tokens.

### BPE Token Segmenter:

1.  **Input:** A new sentence (test data).
2.  **Process:**
    *   Break down each word in the test sentence into its sequence of characters, adding the end-of-word symbol `</w>`.
    *   Apply the merge rules learned during the *training* phase.
    *   Crucially, apply the merges **in the order they were learned**. This is a **greedy** process based on training set frequencies.
    *   Example: If `e + r -> er` was merge #1 and `er + </w> -> er</w>` was merge #2, first replace all `e r` with `er`, then replace all `er </w>` with `er</w>`.
3.  **Output:** The test sentence segmented into tokens from the learned BPE vocabulary.

### Example Walkthrough:

*   **Corpus:** `low (5)`, `lowest (2)`, `newer (6)`, `wider (3)`, `new (2)`
*   **Initial Vocab:** `d, e, i, l, n, o, r, s, t, w, </w>`
*   **Initial Representation:** `l o w </w>`, `l o w e s t </w>`, `n e w e r </w>`, `w i d e r </w>`, `n e w </w>` (with counts)
*   **Merge 1:** `e + r -> er` (count 6+3=9). Vocab adds `er`. Corpus contains `n e w er </w>`, `w i d er </w>`, etc.
*   **Merge 2:** `er + </w> -> er</w>` (count 6+3=9). Vocab adds `er</w>`. Corpus contains `n e w er</w>`, `w i d er</w>`, etc.
*   **Merge 3:** `n + e -> ne` (count 6+2=8). Vocab adds `ne`. Corpus contains `ne w er</w>`, `ne w </w>`, etc.
*   **Later Merges might include:** `(ne, w) -> new`, `(l, o) -> lo`, `(lo, w) -> low`, `(new, er</w>) -> newer</w>`, `(low, </w>) -> low</w>`.
*   **Segmentation Example:**
    *   Test word "lower": -> `l o w e r </w>` -> `l o w er </w>` (Merge 1) -> `l o w er</w>` (Merge 2). If `low` was learned later (e.g., `l+o->lo`, `lo+w->low`), it might become `low er</w>`. The final segmentation depends on the learned merges and their order.
    *   Test word "newer": -> `n e w e r </w>` -> `n e w er </w>` -> `n e w er</w>` -> `ne w er</w>` -> `new er</w>` -> `newer</w>`. If `newer</w>` was learned as a single token, the word is segmented into just that one token.

💡 **Tip: Greedy Segmentation:** The segmenter uses the *learned merge order* greedily. It doesn't re-calculate frequencies on the test set. This makes segmentation fast and deterministic once the vocabulary is learned.

### Outcome:

*   Frequent words in the training data tend to become single tokens in the final vocabulary.
*   Rare words and unknown words are broken down into known, smaller subword units.
*   Vocabulary size is controlled by the number of merges (`k`).
*   Handles morphology implicitly to some extent (e.g., learning "er", "est").
*   The name "Byte-Pair" comes from applying this to sequences of bytes rather than characters, making it language/encoding agnostic, though the example uses characters for clarity.

## 2.6 Word Normalization, Lemmatization and Stemming

### Word Normalization

*   **Definition:** The task of putting words/tokens into a standard, consistent format.
*   **Goal:** To ensure that variations of a word are treated uniformly when needed.
*   **Examples:**
    *   Mapping `USA` and `US` to a single form.
    *   Mapping `uh-huh` and `uhhuh` to a single form.
*   **Trade-off:** Normalization simplifies processing and aids generalization but can lose potentially useful surface information (e.g., the specific spelling choice).
*   **Relation to BPE:** Systems using subword tokenization (like BPE) might inherently handle some variations without explicit normalization steps, as different forms might share common subword tokens.

### Case Folding

*   **Definition:** The simplest form of normalization; converting all text to a single case (usually lowercase).
*   **Benefit:** Allows words like `Woodchuck` and `woodchuck` to be treated identically. Improves generalization, especially for tasks like Information Retrieval (IR) and Speech Recognition.
*   **Drawback:** Loses case information which can be crucial for meaning (`US` vs. `us`, proper nouns vs. common nouns).
*   **Task Dependency:**
    *   **Often Used:** IR, Speech Recognition.
    *   **Often Avoided:** Sentiment Analysis, Text Classification, Information Extraction (IE), Machine Translation (MT) where case distinctions are important.
*   **Practice:** Sometimes models are trained in both cased and uncased versions.

### Lemmatization

*   **Definition:** The task of reducing different inflected forms of a word to its base or dictionary form, known as the **lemma**.
*   **Goal:** Group words with the same root meaning, despite surface differences in form (inflections).
*   **Examples:**
    *   `am`, `are`, `is` -> lemma: `be`
    *   `cat`, `cats` -> lemma: `cat`
    *   `dinner`, `dinners` -> lemma: `dinner`
    *   Polish: `Warszawa`, `Warszawie`, `Warszawy` -> lemma: `Warsaw` (conceptual example)
*   **Lemmatized Sentence Example:** "He is reading detective stories" -> "He be read detective story"
*   **Method:** Requires understanding word structure (**morphology**).
    *   **Morpheme:** Smallest meaning-bearing unit.
    *   **Stem:** The central morpheme carrying the main meaning (e.g., `cat` in `cats`).
    *   **Affix:** Morphemes added to stems (prefixes, suffixes) carrying additional meaning (e.g., `-s` in `cats`).
    *   Sophisticated lemmatizers perform **morphological parsing** (analyzing a word into its constituent morphemes and their features).

    🤔 **Understanding Lemma:** Think of the lemma as the word you would look up in a dictionary (e.g., `be`, `cat`, `run`). Lemmatization aims to map all the variations (`am`, `is`, `are`; `cat`, `cats`; `run`, `ran`, `running`) back to this dictionary form.

### Stemming

*   **Definition:** A simpler, cruder method than lemmatization for reducing words to a "root" form, called the **stem**.
*   **Method:** Typically involves applying heuristic rules to chop off word endings (affixes). Does *not* usually rely on linguistic dictionaries or full morphological analysis.
*   **Example Algorithm:** **Porter Stemmer** (Porter, 1980). Uses multiple passes of rules like:
    *   `ATIONAL` -> `ATE` (e.g., `relational` -> `relate`)
    *   `ING` -> `` (if stem has vowel) (e.g., `motoring` -> `motor`)
    *   `SSES` -> `SS` (e.g., `grasses` -> `grass`)
*   **Stemmed Text Example:** "This was not the map..." -> "Thi wa not the map..." (Note the potentially non-linguistic stems like "Thi", "wa", "copi").
*   **Pros:** Simple, fast. Can be useful for collapsing variants in some applications (like IR).
*   **Cons:**
    *   Crude: Often produces stems that are not actual words.
    *   Error-prone:
        *   **Over-stemming:** Reducing words with different meanings to the same stem (e.g., `policy` -> `polic`).
        *   **Under-stemming:** Failing to reduce related words to the same stem (e.g., `European` not reduced to `Europe`).
    *   Less common in modern NLP systems compared to lemmatization or subword tokenization due to lower accuracy.

    💡 **Tip: Stemming vs. Lemmatization:**
    *   **Lemmatization:** Aims for the *actual* dictionary form (lemma), linguistically principled, more complex, more accurate.
    *   **Stemming:** Uses crude chopping rules to get a *reduced* form (stem), simpler, faster, less accurate, stem might not be a real word.

## 2.7 Sentence Segmentation

*   **Definition:** The task of dividing text into individual sentences. Also called sentence boundary detection.
*   **Importance:** A fundamental step for many NLP tasks that operate on sentence-level units.
*   **Primary Cues:** Punctuation marks like periods (`.`), question marks (`?`), exclamation points (`!`).
*   **Challenge: Period Ambiguity:**
    *   `?` and `!` are relatively unambiguous sentence terminators.
    *   `.` is ambiguous: It can mark the end of a sentence OR be part of an abbreviation (`Mr.`, `Inc.`, `U.S.A.`) or number (`12.40`).
    *   A period can even serve both roles simultaneously (e.g., the period after `Inc.` at the end of a sentence).
*   **Solutions:**
    *   Often addressed **jointly** with word tokenization (how a period is tokenized determines its function).
    *   Use **rules** or **machine learning** models to classify periods.
    *   Employ **abbreviation dictionaries** (hand-built or learned) to identify periods within known abbreviations.
*   **Example Implementation (Stanford CoreNLP):** Uses a rule-based approach where a sentence ends if sentence-ending punctuation (`.`, `!`, `?`) is *not* already part of a recognized token (like an abbreviation or number), possibly followed by closing quotes/brackets.

    💡 **Tip: Period Disambiguation is Key:** Successfully handling the different uses of the period is the core challenge in sentence segmentation for languages like English. Modern toolkits often have sophisticated rules or models for this.

## 2.8 Minimum Edit Distance

* Watch YouTube for Dynamic Programming.
