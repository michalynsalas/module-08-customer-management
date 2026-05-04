# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "IT Support": 90
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "ABC Corp",
    "contact_person": "John Smith",
    "email": "john@abccorp.com",
    "phone": "555-1111"
}

customer2 = {
    "company_name": "TechNova",
    "contact_person": "Lisa Ray",
    "email": "lisa@technova.com",
    "phone": "555-2222"
}

customer3 = {
    "company_name": "GreenLeaf Inc",
    "contact_person": "Michael Brown",
    "email": "michael@greenleaf.com",
    "phone": "555-3333"
}

customer4 = {
    "company_name": "Skyline Solutions",
    "contact_person": "Anna White",
    "email": "anna@skyline.com",
    "phone": "555-4444"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)

for cid, info in customers.items():
    print(f"Customer ID: {cid}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Technology"

print("\nUpdating Customer Information:")
print("-" * 60)
print(customers["C001"])
print(customers["C002"])

# TODO 7: Create project dictionaries
projects = {
    "C001": [
        {"name": "Website Upgrade", "service": "Web Development", "hours": 100, "budget": 15000},
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 40, "budget": 8800}
    ],
    "C002": [
        {"name": "Data Dashboard", "service": "Data Analysis", "hours": 60, "budget": 10500}
    ],
    "C003": [
        {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 80, "budget": 16000}
    ],
    "C004": [
        {"name": "Help Desk Setup", "service": "IT Support", "hours": 50, "budget": 4500}
    ]
}

print("\nProject Information:")
print("-" * 60)
for cid, plist in projects.items():
    for p in plist:
        print(cid, p)

# TODO 8: Calculate project costs
print("\nProject Cost Calculations:")
print("-" * 60)

for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print(p["name"], "| Cost:", cost)

# TODO 9: Customer statistics
print("\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", list(customers.keys()))
print("Companies:", [c["company_name"] for c in customers.values()])
print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
service_counts = {}

for plist in projects.values():
    for p in plist:
        s = p["service"]
        service_counts[s] = service_counts.get(s, 0) + 1

print("\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial aggregations
all_projects = [p for plist in projects.values() for p in plist]

total_hours = sum(p["hours"] for p in all_projects)
total_budget = sum(p["budget"] for p in all_projects)
avg_budget = total_budget / len(all_projects)
max_budget = max(p["budget"] for p in all_projects)
min_budget = min(p["budget"] for p in all_projects)

print("\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary report
print("\nCustomer Summary Report:")
print("-" * 60)

for cid, cust in customers.items():
    plist = projects.get(cid, [])
    hours = sum(p["hours"] for p in plist)
    budget = sum(p["budget"] for p in plist)

    print(cid, cust["company_name"])
    print("Projects:", len(plist))
    print("Total Hours:", hours)
    print("Total Budget:", budget)
    print()

# TODO 13: Rate adjustments
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers with projects
active_customers = {cid: customers[cid] for cid in customers if cid in projects}

print("\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Customer budget totals
customer_budgets = {
    cid: sum(p["budget"] for p in plist)
    for cid, plist in projects.items()
}

print("\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service pricing tiers
service_tiers = {
    s: "Premium" if r >= 200 else "Standard" if r >= 100 else "Basic"
    for s, r in services.items()
}

print("\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    for field in required:
        if field not in customer_dict:
            return False
    return True

print("\nCustomer Validation:")
print("-" * 60)

for cid, cust in customers.items():
    print(cid, validate_customer(cust))

# TODO 18: Project status tracking
print("\nProject Status Summary:")
print("-" * 60)

status_counts = {"active": 0, "completed": 0, "pending": 0}

status_counts = {"active": 0, "completed": 0, "pending": 0}

statuses = ["active", "completed", "pending"]
i = 0

for plist in projects.values():
    for p in plist:
        p["status"] = statuses[i % 3]	# cycle through statuses
        status_counts[p["status"]] += 1
        i += 1

print(status_counts)

# TODO 19: Budget analysis function
def analyze_customer_budgets(projects_dict):
    results = {}

    for cid, plist in projects_dict.items():
        budgets = [p["budget"] for p in plist]
        total = sum(budgets)
        count = len(budgets)
        average = total / count if count > 0 else 0

        results[cid] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results

print("\nDetailed Budget Analysis:")
print("-" * 60)
print(analyze_customer_budgets(projects))

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):

    used_services = set()

    for p in projects.get(customer_id, []):
        used_services.add(p["service"])

    recommendations = []

    for s in services:
        if s not in used_services:
            recommendations.append(s)

    return recommendations


print("\nService Recommendations:")
print("-" * 60)

for cid in customers:
    print(cid, recommend_services(cid, customers, projects, services))