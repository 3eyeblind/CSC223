from .triage import TriageSystem

def run_demo():
    patients = [
        ("Sofia", 5), ("Bob", 2), ("Charlie", 4), ("Diana", 3),
        ("Eli", 1), ("Tom", 4), ("Alice", 5), ("Rachel", 4),
    ]
    TriageSystem._arrival_counter = 0  # reset 
    t = TriageSystem()
    t.load(patients)

    print("Processing patients:")
    while not t.IsEmpty():
        name, sev = t.ProcessNext()
        print(f"Now treating: {name} (Severity {sev})")

if __name__ == "__main__":
    run_demo()