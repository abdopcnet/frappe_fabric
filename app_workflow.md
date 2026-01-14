# Application Workflow Diagrams

Workflow documentation for Frappe Fabric Management application processes.

## Main Workflows

### 1. Container Receipt Workflow

```
Container Arrives
       │
       ▼
Create Container Receipt
- Container Number
- Supplier
- Expected Items
       │
       ▼
Scan Rolls
- QR Code Scan
- Measure Length
- Assign Location
       │
       ▼
Create Fabric Roll Records
- Auto-generate Roll Number
- Link to Receipt
       │
       ▼
Submit Receipt
- Update Expected vs Received
- Create Movements
       │
       ▼
Rolls Available in Warehouse
```

### 2. Sample Cutting Workflow

```
Select Roll(s)
       │
       ▼
Create Sample Cutting
- Purpose
- Expense Account
- Cut Quantities
       │
       ▼
Submit Cutting
- Reduce Roll Length
- Create GL Entry
- Create Movement
       │
       ▼
Roll Updated
Accounting Posted
```

### 3. Retail Sale Workflow

```
Customer Request
- Select Roll
- Specify Quantity
       │
       ▼
Create Retail Cutting Sale
- Roll Number
- Cut Quantity
- Rate
- Sale Type
       │
       ▼
Submit Sale
- Reduce Roll
- Create Sales Invoice (if credit)
- Create Movement
       │
       ▼
Sale Completed
Roll Updated
```

### 4. Roll Transfer Workflow

```
Select Roll(s) for Transfer
       │
       ▼
Create Roll Transfer
- Source Warehouse
- Target Warehouse
- Roll Numbers
       │
       ▼
Submit Transfer
- Update Warehouse
- Create Movement Records
       │
       ▼
Rolls Transferred to New Warehouse
```

## Data Flow Diagrams

### Roll Lifecycle

```
Container Receipt
       │ Creates
       ▼
Fabric Roll (Available)
       │
       ├─ Sample Cut
       │
       └─ Retail Sale
              │
              ▼
       Roll Length Reduced
              │
              ▼
       Roll (Exhausted)
```

### Movement Tracking

Every transaction creates a Roll Movement record with:
- Roll Number
- Movement Type
- Quantity
- Balance Before
- Balance After
- Warehouse
- Reference Document

This links to the Fabric Roll which tracks:
- current_length
- last_movement_date
- last_movement_type

## State Transitions

### Roll Status States

```
Available → Reserved → Available
    │                      │
    │ Sample Cut           │ Retail Sale
    │                      │
    ▼                      ▼
Consumed              Consumed
    │                      │
    └──────────┬───────────┘
               │
               ▼
          Exhausted
```

### Container Receipt States

```
Draft → In Progress → Completed
  │                      │
  └──────────Cancel──────┘
```

### Transaction States

```
Draft → Submitted → Cancelled
  │        │
  │        └→ (Cannot Cancel)
  │
  └→ (Can Cancel)
```

## Integration Points

### Accounting Integration

- Sample Cutting → GL Entry (Expense)
- Retail Sale → Sales Invoice (if Credit)
- Roll Receipt → Purchase Receipt (linked)

### ERPNext Integration

- Fabric Roll → Item (via is_fabric_item)
- Container Receipt → Purchase Receipt
- Retail Sale → Sales Invoice
- Warehouse → Standard Warehouse

## API Workflow

### Typical API Usage Flow

```
1. Authentication
   ↓
2. GET/Search Operations
   ↓
3. CREATE Operations
   ↓
4. UPDATE Operations
   ↓
5. Submit Documents
   ↓
6. GET Reports
```

### Error Handling Flow

```
API Request
    ↓
Validation
    ↓
┌───┴───┐
│ Valid │ Invalid
└───┬───┘    │
    │        │
    ▼        ▼
Process   Return Error
    │        │
    │        └─→ HTTP 400/500
    │
    ▼
Return Success
    │
    └─→ HTTP 200
```

## Business Rules

### Roll Management Rules

1. Roll Creation: Only via Container Receipt
2. Roll Update: Length can only decrease (consumption)
3. Roll Transfer: Must update both source and target warehouses
4. Roll Reservation: Cannot reserve more than available length

### Transaction Rules

1. Sample Cutting: Requires expense account
2. Retail Sale: Can be cash or credit
3. Container Receipt: Tracks expected vs received
4. All Transactions: Create movement records

### Accounting Rules

1. Sample Cutting: Debit expense account, Credit inventory
2. Retail Sale: Debit cash/receivable, Credit sales, Debit COGS
3. Movements: Track all changes for audit trail
