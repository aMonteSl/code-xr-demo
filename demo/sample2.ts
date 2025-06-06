interface User {
  id: number;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'moderator';
}

class UserManager {
  private users: Map<number, User> = new Map();
  private nextId: number = 1;

  // Low complexity
  addUser(name: string, email: string, role: User['role'] = 'user'): User {
    const user: User = {
      id: this.nextId++,
      name,
      email,
      role
    };
    this.users.set(user.id, user);
    return user;
  }

  // Medium complexity
  findUsers(criteria: Partial<User>): User[] {
    const results: User[] = [];
    
    for (const user of this.users.values()) {
      let matches = true;
      
      if (criteria.id !== undefined && user.id !== criteria.id) {
        matches = false;
      }
      if (criteria.name !== undefined && !user.name.toLowerCase().includes(criteria.name.toLowerCase())) {
        matches = false;
      }
      if (criteria.email !== undefined && user.email !== criteria.email) {
        matches = false;
      }
      if (criteria.role !== undefined && user.role !== criteria.role) {
        matches = false;
      }
      
      if (matches) {
        results.push(user);
      }
    }
    
    return results;
  }

  // High complexity
  generateUserReport(): string {
    let report = "=== USER REPORT ===\n";
    const roleStats: Record<string, number> = {};
    const emailDomains: Record<string, number> = {};
    
    for (const user of this.users.values()) {
      // Count roles
      if (roleStats[user.role]) {
        roleStats[user.role]++;
      } else {
        roleStats[user.role] = 1;
      }
      
      // Extract and count email domains
      const emailParts = user.email.split('@');
      if (emailParts.length === 2) {
        const domain = emailParts[1].toLowerCase();
        if (emailDomains[domain]) {
          emailDomains[domain]++;
        } else {
          emailDomains[domain] = 1;
        }
      }
    }
    
    report += `\nTotal Users: ${this.users.size}\n`;
    report += "\nRole Distribution:\n";
    
    for (const [role, count] of Object.entries(roleStats)) {
      const percentage = ((count / this.users.size) * 100).toFixed(1);
      report += `  ${role}: ${count} (${percentage}%)\n`;
    }
    
    report += "\nTop Email Domains:\n";
    const sortedDomains = Object.entries(emailDomains)
      .sort(([,a], [,b]) => b - a)
      .slice(0, 5);
      
    for (const [domain, count] of sortedDomains) {
      report += `  ${domain}: ${count} users\n`;
    }
    
    return report;
  }
}

// Demo usage
const userManager = new UserManager();
userManager.addUser("Alice Smith", "alice@example.com", "admin");
userManager.addUser("Bob Johnson", "bob@gmail.com", "user");
userManager.addUser("Carol Davis", "carol@example.com", "moderator");
userManager.addUser("David Wilson", "david@yahoo.com", "user");

console.log(userManager.generateUserReport());