using Microsoft.EntityFrameworkCore;
using Vidly.Models;

namespace Vidly.Data
{
    public class VidlyDbContext : DbContext
    {
        public DbSet<Expense> Expenses { get; set; } 

        public VidlyDbContext(DbContextOptions<VidlyDbContext> options) : base(options)
        {
            
        }
    }
}
