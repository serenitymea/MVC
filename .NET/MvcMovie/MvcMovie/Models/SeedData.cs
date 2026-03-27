using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using MvcMovie.Data;
using System;
using System.Linq;

namespace MvcMovie.Models
{
    public static class SeedData
    {
        public static void Initialize(IServiceProvider serviceProvider)
        {
            using (var context = new MvcMovieContext(
                serviceProvider.GetRequiredService<DbContextOptions<MvcMovieContext>>()))
            {

                if (context.Movie.Any())
                {
                    return;
                }

                context.Movie.AddRange(
                    new Movie
                    {
                        Title = "hyhyhyhyh",
                        ReleaseDate = DateTime.Parse("1989-1-11"),
                        Genre = "comedy",
                        Price = 600
                    },

                    new Movie
                    {
                        Title = "adasdasdasddas",
                        ReleaseDate = DateTime.Parse("1984-3-13"),
                        Genre = "art",
                        Price = 300
                    },

                    new Movie
                    {
                        Title = "asdasdasdasdasddas",
                        ReleaseDate = DateTime.Parse("1989-6-16"),
                        Genre = "comedy",
                        Price = 700
                    },

                    new Movie
                    {
                        Title = "sdadsdsa",
                        ReleaseDate = DateTime.Parse("1959-4-15"),
                        Genre = "art",
                        Price = 900
                    }
                );

                context.SaveChanges();
            }
        }
    }
}