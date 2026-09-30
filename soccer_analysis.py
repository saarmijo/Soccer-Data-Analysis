import pandas as pd
import matplotlib.pyplot as plt

# CSE 310 - Data Analysis Module
# Soccer / International Football Results
# This program analyzes international soccer match results.
# It answers two questions using Pandas and creates a graph as a stretch challenge.

DATA_FILE = "results.csv"
MINIMUM_MATCHES = 100
TOP_TEAMS = 10


def load_data():
    """Load the soccer results CSV into a Pandas DataFrame."""
    print("\nLoading soccer data...")
    data = pd.read_csv(DATA_FILE)

    print(f"Loaded {len(data):,} matches.")
    print(f"Columns available: {len(data.columns)}")
    return data


def clean_data(data):
    """Prepare the columns needed for the analysis."""
    print("\nCleaning the data...")

    needed_columns = [
        "date",
        "home_team",
        "away_team",
        "home_score",
        "away_score",
        "tournament",
    ]

    data = data[needed_columns].copy()

    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    data["home_score"] = pd.to_numeric(data["home_score"], errors="coerce")
    data["away_score"] = pd.to_numeric(data["away_score"], errors="coerce")

    data = data.dropna(
        subset=["home_team", "away_team", "home_score", "away_score"]
    )

    print(f"Usable matches after cleaning: {len(data):,}")
    return data


def create_team_data(data):
    """Create one row for every team's performance in every match."""

    home_data = data[
        ["date", "home_team", "home_score", "away_score", "tournament"]
    ].copy()

    home_data = home_data.rename(
        columns={
            "home_team": "team",
            "home_score": "goals_scored",
            "away_score": "goals_conceded",
        }
    )

    home_data["location"] = "Home"

    away_data = data[
        ["date", "away_team", "away_score", "home_score", "tournament"]
    ].copy()

    away_data = away_data.rename(
        columns={
            "away_team": "team",
            "away_score": "goals_scored",
            "home_score": "goals_conceded",
        }
    )

    away_data["location"] = "Away"

    team_data = pd.concat(
        [home_data, away_data],
        ignore_index=True,
    )

    return team_data


def calculate_team_statistics(team_data):
    """Aggregate match-level data into team-level statistics."""

    statistics = (
        team_data.groupby("team")
        .agg(
            matches=("team", "count"),
            total_goals=("goals_scored", "sum"),
            average_goals=("goals_scored", "mean"),
            goals_conceded=("goals_conceded", "sum"),
        )
        .reset_index()
    )

    statistics["average_goals"] = statistics["average_goals"].round(2)

    return statistics


def question_one(statistics):
    """Answer Question 1: Which teams scored the most total goals?"""

    print("\nQUESTION 1")
    print("Which teams have scored the most goals in the dataset?")
    print("-" * 60)

    results = statistics.sort_values(
        by="total_goals",
        ascending=False,
    ).head(TOP_TEAMS)

    print(
        results[
            ["team", "matches", "total_goals"]
        ].to_string(index=False)
    )

    return results


def question_two(statistics):
    """Answer Question 2 using a minimum-match filter and average."""

    print("\nQUESTION 2")
    print("Which teams have the highest average goals per match?")
    print(
        f"(Only teams with at least {MINIMUM_MATCHES} matches are included.)"
    )
    print("-" * 60)

    filtered = statistics[
        statistics["matches"] >= MINIMUM_MATCHES
    ].copy()

    results = filtered.sort_values(
        by="average_goals",
        ascending=False,
    ).head(TOP_TEAMS)

    print(
        results[
            ["team", "matches", "average_goals"]
        ].to_string(index=False)
    )

    return results


def show_basic_summary(data):
    """Display a few basic facts about the dataset."""

    print("\nDATASET SUMMARY")
    print("-" * 60)
    print(f"Number of matches: {len(data):,}")
    print(f"Number of tournaments: {data['tournament'].nunique():,}")
    print(
        f"Date range: "
        f"{data['date'].min().date()} to {data['date'].max().date()}"
    )
    print(
        f"Average goals per match: "
        f"{(data['home_score'] + data['away_score']).mean():.2f}"
    )


def create_graph(results):
    """Create a bar graph for the top teams by total goals."""

    print("\nCreating graph...")

    graph_data = results.sort_values(
        by="total_goals",
        ascending=True,
    )

    plt.figure(figsize=(10, 6))
    plt.barh(
        graph_data["team"],
        graph_data["total_goals"],
    )
    plt.xlabel("Total Goals")
    plt.ylabel("Team")
    plt.title("Top International Teams by Total Goals")
    plt.tight_layout()
    plt.show()


def save_results(question_one_results, question_two_results):
    """Save the two answers to CSV files for documentation."""

    question_one_results.to_csv(
        "question1_results.csv",
        index=False,
    )

    question_two_results.to_csv(
        "question2_results.csv",
        index=False,
    )

    print("\nResults were saved to CSV files.")


def display_menu():
    """Display the program menu."""

    print("\n" + "=" * 60)
    print("SOCCER DATA ANALYSIS")
    print("=" * 60)
    print("1. Show dataset summary")
    print("2. Answer Question 1")
    print("3. Answer Question 2")
    print("4. Create graph")
    print("5. Save analysis results")
    print("6. Run all analysis")
    print("7. Exit")
    print("=" * 60)


def run_program():
    """Run the interactive analysis program."""

    data = load_data()
    data = clean_data(data)

    team_data = create_team_data(data)
    statistics = calculate_team_statistics(team_data)

    question_one_results = None
    question_two_results = None

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_basic_summary(data)

        elif choice == "2":
            question_one_results = question_one(statistics)

        elif choice == "3":
            question_two_results = question_two(statistics)

        elif choice == "4":
            if question_one_results is None:
                question_one_results = question_one(statistics)

            create_graph(question_one_results)

        elif choice == "5":
            if question_one_results is None:
                question_one_results = question_one(statistics)

            if question_two_results is None:
                question_two_results = question_two(statistics)

            save_results(
                question_one_results,
                question_two_results,
            )

        elif choice == "6":
            show_basic_summary(data)

            question_one_results = question_one(statistics)
            question_two_results = question_two(statistics)

            create_graph(question_one_results)

            save_results(
                question_one_results,
                question_two_results,
            )

        elif choice == "7":
            print("\nThank you for using Soccer Data Analysis!")
            break

        else:
            print("\nPlease enter a number from 1 to 7.")


if __name__ == "__main__":
    run_program()
