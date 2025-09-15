# Auto Ticketing Machine - Program Log

## Program Overview
**File:** `autoticketingMachine.py`  
**Purpose:** Automated train ticket purchasing system for Hanoi - Saigon route (Train SE7)  
**Algorithm Used:** Greedy algorithm for change calculation  
**Date:** September 14, 2025  

## Program Structure and Flow

### 1. Ticket Price Display
```
Displays available ticket types with prices:
- Type 1: Air-conditioned sleeper car 4 beds T2 - 1,609,000 VND
- Type 2: Air-conditioned sleeper car 6 beds T1 - 1,444,000 VND  
- Type 3: Air-conditioned sleeper car 6 beds T3 - 1,146,000 VND
- Type 4: Air-conditioned soft seat - 966,000 VND
- Type 5: Air-conditioned hard seat - 744,000 VND
- Type 6: Additional seat - 524,000 VND
```

### 2. User Input Validation Process

#### Ticket Type Selection
- **Input Range:** 1-6 (integer)
- **Validation:** Loops until valid input (1 ≤ userChoice ≤ 6)
- **Error Handling:** Prompts user to re-enter if invalid

#### Ticket Quantity Selection  
- **Input Range:** Positive integers only
- **Validation:** Loops until numberOfTicket > 0
- **Error Handling:** Displays "Number of tickets must be greater than 0!"

### 3. Price Calculation Logic
Uses Python's `match-case` statement (Python 3.10+):
```python
Price Mapping:
- Case 1 → 1609K VND
- Case 2 → 1444K VND  
- Case 3 → 1146K VND
- Case 4 → 966K VND
- Case 5 → 744K VND
- Default → 524K VND
```

**Total Cost Formula:** `cost = ticketPrice × numberOfTicket`

### 4. Payment Processing

#### Payment Input
- **Requirement:** paid ≥ cost
- **Validation:** Loops until sufficient payment received
- **Error Handling:** "Amount insufficient, please re-enter!"

#### Change Calculation
- **Formula:** `change = paid - cost`
- **Algorithm:** Greedy approach using largest denomination first

### 5. Greedy Change Algorithm Implementation

#### Denomination Array
```python
denoms = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # in thousands VND
```

#### Algorithm Steps
1. **Initialize:** Empty breakdown list, counter = 0
2. **For each denomination:**
   - Calculate: `temp = change // denomination`
   - Update: `change %= denomination`
   - Increment: `counter += temp`
   - Record: If temp > 0, add to breakdown list
3. **Output:** Total bills count and detailed breakdown

### 6. Output Format

#### Invoice Display
```
Format: "Your invoice: [price] x [quantity] = [total] K"
Example: "Your invoice: 1609 x 2 = 3218 K"
```

#### Change Breakdown
```
Format: "Number of bills to return: [count] bills"
Detail format: "- [quantity] x [denomination]K"
Example: 
- 3 x 500K
- 1 x 200K
- 1 x 50K
```

## Key Features

### 1. Input Validation
- **Robust Error Handling:** All user inputs validated with appropriate error messages
- **Type Safety:** Integer conversion with proper exception handling expected
- **Range Checking:** Ensures logical input ranges for all parameters

### 2. Greedy Algorithm Efficiency
- **Time Complexity:** O(n) where n = number of denominations (9)
- **Space Complexity:** O(n) for breakdown storage
- **Optimality:** Provides minimum number of bills for change

### 3. User Experience
- **Clear Instructions:** Vietnamese language interface for local users
- **Immediate Feedback:** Real-time validation and error messages
- **Detailed Output:** Complete transaction summary with change breakdown

## Program Execution Flow Chart
```
START
  ↓
Display Ticket Prices
  ↓
Get Ticket Type (1-6) [Loop until valid]
  ↓
Get Ticket Quantity [Loop until > 0]
  ↓
Calculate Total Cost
  ↓
Get Payment Amount [Loop until >= cost]
  ↓
Calculate Change
  ↓
Apply Greedy Algorithm for Change Breakdown
  ↓
Display Results (Bills count + breakdown)
  ↓
END
```

## Technical Implementation Notes

### Language Features Used
- **Match-Case Statement:** Modern Python syntax (3.10+)
- **F-string Formatting:** For clean output display
- **List Comprehension:** For breakdown collection
- **Integer Division:** `//` operator for exact bill counting
- **Modulo Operation:** `%` operator for remaining change

### Code Quality Aspects
- **Single Responsibility:** Each section handles one specific task
- **Input Validation:** Comprehensive error checking
- **Clear Variable Names:** Self-documenting code structure
- **Consistent Formatting:** Well-organized code layout

## Potential Improvements
1. **Exception Handling:** Add try-catch for non-integer inputs
2. **Configuration:** External price configuration file
3. **Logging:** Add transaction logging to file
4. **Internationalization:** Multi-language support
5. **GUI Interface:** Graphical user interface option

## Algorithm Analysis
The greedy approach works optimally for this Vietnamese currency system because:
- Denominations follow a pattern where larger denominations are multiples or near-multiples of smaller ones
- No denomination combination can create a more efficient solution than using the largest possible denomination first
- Standard currency design ensures greedy algorithm optimality

---
**Log Generated:** September 14, 2025  
**Program Version:** Python 3.10+  
**Status:** Functional and Complete